from system_design.kv_store.engine.record import Record
from system_design.kv_store.engine.clock import Clock, SystemClock
from system_design.kv_store.engine.expiration_entry import ExpirationEntry
from system_design.kv_store.engine.expiration_manager import ExpirationManager


class KVStore:

    def __init__(self, clock: Clock | None = None, expiration_manager=None):
        self._store = {}
        self._clock = clock or SystemClock()
        self._expiration_manager = expiration_manager or ExpirationManager()

    def put(self, key: str, value: object, ttl: float | None = None):
        if ttl is None:
            expires_at = None
        else:
            expires_at = self._clock.now() + ttl

        self._store[key] = Record(value=value, expires_at=expires_at)

        # register entry for expiration schedule
        if expires_at is not None:
            self._expiration_manager.register(key=key, expires_at=expires_at)

    def get(self, key: str):

        record = self._get_record(key)

        if record is None:
            return None

        return record.value

    def delete(self, key: str):
        return self._delete(key)

    def exists(self, key: str):
        return self._get_record(key) is not None

    # remove the expired entries
    def cleanup(self) -> None:
        current_time = self._clock.now()
        expired_entries = self._expiration_manager.cleanup_schedule(current_time)

        for entry in expired_entries:
            self._remove_if_expired(entry)

    # update the expiring time
    def set_ttl(self, key: str, ttl: float | None = None) -> bool:
        record = self._get_record(key)

        if not (record):
            return False

        expires_at = self._clock.now() + ttl

        record.expires_at = expires_at

        self._expiration_manager.register(key, expires_at)

        return True

    # remove expiration
    def persist(self, key: str) -> bool:
        record = self._get_record(key)

        if not (record):
            return False

        record.expires_at = None

        return True

    def _get_record(self, key: str) -> Record | None:

        record = self._store.get(key)

        if record is None:
            return None

        if record.is_expired(self._clock.now()):
            del self._store[key]
            return None

        return record

    def _delete(self, key: str):

        if key in self._store:
            del self._store[key]
            return True
        else:
            return False

    def _remove_if_expired(self, entry: ExpirationEntry):

        record = self._store.get(entry.key)

        if record is None:
            return

        if record.expires_at != entry.expires_at:
            return  # stale heap entry

        self._delete(entry.key)


def main() -> None:
    "Entry point for manual execution."
    pass


if __name__ == "__main__":
    main()
