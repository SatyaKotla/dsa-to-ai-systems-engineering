from system_design.kv_store.engine.store import KVStore


class BackgroundCleaner:

    def __init__(self, store: KVStore, interval: float = 1.0):
        self._store = store
        self._interval = interval

    def run_once(self) -> None:
        self._store.cleanup()
