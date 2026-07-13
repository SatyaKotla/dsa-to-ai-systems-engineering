from system_design.kv_store.engine.record import Record
from system_design.kv_store.engine.clock import SystemClock


class KVStore:

    def __init__(self, clock: SystemClock | None = None):
        self._store = {}
        self._clock = clock or SystemClock()

    def put(self, key: str, value: object, ttl: float | None = None):
        if ttl is None:
            expires_at = None
        else:
            expires_at = self._clock.now() + ttl

        self._store[key] = Record(value=value, expires_at=expires_at)

    def get(self, key: str):

        record = self._get_record(key)

        if record is None:
            return None

        return record.value

    def delete(self, key: str):

        if key in self._store:
            del self._store[key]
            return True
        else:
            return False

    def exists(self, key: str):
        return self._get_record(key) is not None

    def _get_record(self, key: str) -> Record | None:

        record = self._store.get(key)

        if record is None:
            return None

        if record.is_expired(self._clock.now()):
            del self._store[key]
            return None

        return record


def main() -> None:
    "Entry point for manual execution."
    import time

    db = KVStore()

    db.put("name", "Gan")

    print(db.get("name") == "Gan")
    print(db.exists("name"))

    db.delete("name")

    print(db.get("name") is None)
    print(not (db.exists("name")))

    db.put("temp", "value", ttl=2)

    print(db.get("temp"))

    time.sleep(3)

    print(db.get("temp"))

    print(db.exists("temp"))


if __name__ == "__main__":
    main()
