from dataclasses import dataclass


@dataclass
class Record:
    value: object
    expires_at: float | None = None

    def is_expired(self, current_time: float) -> bool:

        if self.expires_at is None:
            return False

        return current_time >= self.expires_at
