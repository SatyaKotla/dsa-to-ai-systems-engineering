from system_design.kv_store.engine.store import KVStore
import threading


class BackgroundCleaner:

    def __init__(self, store: KVStore, interval: float = 1.0):
        self._store = store
        self._interval = interval

        self._stop_event = (
            threading.Event()
        )  # traffic light (red or green) intial green

        self._thread = None  # to keep the background workers

    def run_once(self) -> None:
        self._store.cleanup()

    def _run(self) -> None:

        while not self._stop_event.is_set():

            self.run_once()

            self._stop_event.wait(self._interval)

    def start(self) -> None:

        if self._thread is not None and self._thread.is_alive():
            return

        self._stop_event.clear()

        self._thread = threading.Thread(target=self._run, daemon=True)

        self._thread.start()

    def stop(self) -> None:

        self._stop_event.set()

        if self._thread is not None:
            self._thread.join()
