####################################################
# --------- TESTS FOR SERVICES COMPONENT ------- ###
####################################################
from unittest.mock import Mock
from system_design.kv_store.services.kv_store_service import KVStoreService


def test_put_delegates_to_store():
    store = Mock()

    service = KVStoreService(store=store)

    service.put(key="A", value=100, ttl=20)

    store.put.assert_called_once_with(key="A", value=100, ttl=20)


def test_get_returns_store_value():

    store = Mock()

    store.get.return_value = 123

    service = KVStoreService(store)

    assert service.get(key="A") == 123

    store.get.assert_called_once_with(key="A")


def test_delete_returns_store_result():

    store = Mock()

    store.delete.return_value = True

    service = KVStoreService(store)

    assert service.delete(key="A") is True

    store.delete.assert_called_once_with(key="A")


def test_exists_returns_store_result():

    store = Mock()

    store.exists.return_value = False

    service = KVStoreService(store)

    assert service.exists(key="A") is False

    store.exists.assert_called_once_with(key="A")


def test_set_ttl_delegates_to_store():

    store = Mock()

    store.set_ttl.return_value = True

    service = KVStoreService(store)

    assert service.set_ttl(key="A", ttl=10) is True

    store.set_ttl.assert_called_once_with(key="A", ttl=10)


def test_persist_delegates_to_store():

    store = Mock()

    store.persist.return_value = True

    service = KVStoreService(store)

    assert service.persist(key="A") is True

    store.persist.assert_called_once_with(key="A")


def test_ttl_returns_store_value():

    store = Mock()

    store.ttl.return_value = 15

    service = KVStoreService(store)

    assert service.ttl(key="A") == 15

    store.ttl.assert_called_once_with(key="A")
