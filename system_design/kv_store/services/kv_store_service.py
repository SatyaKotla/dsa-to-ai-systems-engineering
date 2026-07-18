from system_design.kv_store.engine.store import KVStore


class KVStoreService:

    def __init__(self, store: KVStore):
        self._store = store

    def put(self, key: str, value: object, ttl: float | None = None) -> None:
        self._store.put(key=key, value=value, ttl=ttl)

    def get(self, key: str) -> object | None:
        return self._store.get(key=key)

    def delete(self, key: str) -> bool:
        return self._store.delete(key=key)

    def exists(self, key: str) -> bool:
        return self._store.exists(key=key)

    def set_ttl(self, key: str, ttl: float | None = None) -> bool:
        return self._store.set_ttl(key=key, ttl=ttl)

    def persist(self, key: str) -> bool:
        return self._store.persist(key=key)

    def ttl(self, key: str) -> float:
        return self._store.ttl(key=key)
