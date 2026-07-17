####################################################
# --------- TESTS FOR ENGINE COMPONENT ------- #
####################################################
from system_design.kv_store.engine.record import Record
from system_design.kv_store.engine.background_cleaner import BackgroundCleaner
from system_design.kv_store.engine.expiration_manager import ExpirationManager
from system_design.kv_store.engine.store import KVStore
from system_design.kv_store.engine.clock import FakeClock
import time


def test_record():

    record = Record(value="A", expires_at=100)

    assert not record.is_expired(99)
    assert not record.is_expired(100 - 0.001)
    assert record.is_expired(100)
    assert record.is_expired(101)


# Expiration manager
def test_expiration_manager():

    manager = ExpirationManager()

    manager.register("A", 100)
    manager.register("B", 200)

    expired = manager.cleanup_schedule(150)

    assert len(expired) == 1
    assert expired[0].key == "A"

    expired = manager.cleanup_schedule(250)

    assert len(expired) == 1
    assert expired[0].key == "B"


# KV Store without TTL
def test_kv_store_without_ttl():
    db = KVStore()

    db.put("name", "Gan")

    assert db.get("name") == "Gan"
    assert db.exists("name")

    db.delete("name")

    assert db.get("name") is None
    assert not db.exists("name")


# Integration test
def test_integration():

    manager = ExpirationManager()

    db = KVStore(expiration_manager=manager)

    cleaner = BackgroundCleaner(store=db)

    db.put("temp", "value", ttl=2)

    time.sleep(3)
    cleaner.run_once()

    assert "temp" not in db._store


# Stale heap entry test
def test_stale_heap_entry():

    manager = ExpirationManager()

    db = KVStore(expiration_manager=manager)

    cleaner = BackgroundCleaner(store=db)

    db.put("A", 1, ttl=2)

    time.sleep(1)

    db.put("A", 1, ttl=10)

    time.sleep(2)

    cleaner.run_once()

    assert db.get("A") == 1


def test_put_registers_expiration():
    db = KVStore()

    db.put("temp", "value", ttl=5)

    assert db._expiration_manager.size() == 1


def test_cleanup_removes_expired_entry_from_heap():
    db = KVStore()

    db.put("temp", "value", ttl=2)

    assert db._expiration_manager.size() == 1

    time.sleep(3)

    db.cleanup()

    assert db._expiration_manager.size() == 0


def test_cleanup_removes_expired_key_from_store():
    db = KVStore()

    db.put("temp", "value", ttl=2)

    time.sleep(3)

    db.cleanup()

    assert "temp" not in db._store


def test_key_without_ttl_is_never_registered():
    db = KVStore()

    db.put("permanent", 100)

    assert db._expiration_manager.size() == 0

    time.sleep(2)

    db.cleanup()

    assert db.get("permanent") == 100


def test_cleanup_on_empty_store():
    db = KVStore()

    db.cleanup()

    assert db._expiration_manager.size() == 0


# test the fakeclock
def test_fake_clock():
    clock = FakeClock()

    db = KVStore(clock=clock)

    db.put("temp", "value", ttl=2)

    clock.advance(3)

    db.cleanup()

    assert db.get("temp") is None


# test the expiry updation
def test_set_ttl():
    clock = FakeClock()

    db = KVStore(clock=clock)

    db.put("A", 100)

    assert db.set_ttl("A", 10)

    clock.advance(11)

    db.cleanup()

    assert db.get("A") is None


# test persist
def test_persist():

    clock = FakeClock()

    db = KVStore(clock=clock)

    db.put("A", 100, ttl=10)

    assert db.persist("A")

    clock.advance(20)

    db.cleanup()

    assert db.get("A") == 100


def test_persist_non_existent_key():
    clock = FakeClock()

    db = KVStore(clock=clock)

    assert db.persist("missing") is False


# ttl
def test_ttl():
    clock = FakeClock()

    db = KVStore(clock=clock)

    db.put("A", 100, ttl=20)

    clock.advance(5)

    assert db.ttl("A") == 15


def test_ttl_permanent_key():
    clock = FakeClock()

    db = KVStore(clock=clock)

    db.put("A", 100)

    assert db.ttl("A") == -1


def test_ttl_missing_key():
    clock = FakeClock()

    db = KVStore(clock=clock)

    assert db.ttl("missing") == -2


def test_ttl_expired_key():
    clock = FakeClock()

    db = KVStore(clock=clock)

    db.put("A", 100, ttl=10)

    clock.advance(15)

    assert db.ttl("A") == -2


# test background cleaner
def test_background_cleaner_removes_expired_key():
    db = KVStore()

    cleaner = BackgroundCleaner(db, interval=0.1)
    cleaner.start()

    try:
        db.put("A", 100, ttl=1)

        time.sleep(1.5)

        assert db.get("A") is None
    finally:
        cleaner.stop()


def test_background_cleaner_does_not_remove_permanent_key():
    db = KVStore()

    cleaner = BackgroundCleaner(db, interval=0.1)
    cleaner.start()

    try:
        db.put("A", 100)

        time.sleep(1.5)

        assert db.get("A") == 100
    finally:
        cleaner.stop()


def test_background_cleaner_ignores_stale_expiration():
    db = KVStore()

    cleaner = BackgroundCleaner(db, interval=0.1)
    cleaner.start()

    try:
        db.put("A", 100, ttl=1)

        time.sleep(0.5)

        db.set_ttl("A", 3)

        time.sleep(1)

        assert db.get("A") == 100

        time.sleep(2.5)

        assert db.get("A") is None

    finally:
        cleaner.stop()
