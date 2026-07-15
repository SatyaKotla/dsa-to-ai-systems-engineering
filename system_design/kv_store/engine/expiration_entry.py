from dataclasses import dataclass


@dataclass(order=True)
class ExpirationEntry:
    expires_at: float
    key: str
