from abc import ABC, abstractmethod
import time


# abstraction
class Clock(ABC):

    @abstractmethod
    def now(self) -> float:
        """Return the current time."""
        pass


# System Clock
class SystemClock(Clock):

    def now(self) -> float:
        return time.time()


# Fake Clock for testing purposes
class FakeClock(Clock):

    def __init__(self, start: float = 0.0):
        self._current_time = start

    def now(self) -> float:
        return self._current_time

    def advance(self, seconds: float) -> None:
        if seconds < 0:
            raise ValueError("Cannot move time backwards.")

        self._current_time += seconds
