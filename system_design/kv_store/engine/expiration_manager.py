import heapq
from system_design.kv_store.engine.expiration_entry import ExpirationEntry


class ExpirationManager:

    def __init__(self):
        self._heap = []

    def register(self, key: str, expires_at: float) -> None:

        heapq.heappush(self._heap, ExpirationEntry(expires_at=expires_at, key=key))

    def cleanup_schedule(self, current_time: float) -> list[ExpirationEntry]:

        expired = []

        while self._heap:

            entry = self._heap[0]  # check the entry

            if entry.expires_at > current_time:
                break

            expired.append(heapq.heappop(self._heap))

        return expired

    def size(self) -> int:
        return len(self._heap)
