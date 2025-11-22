from dataclasses import dataclass, field

@dataclass
class Process:
    pid: int
    arrival: float = 0.0
    burst: float = 1.0
    remaining: float = field(default=None)
    priority: int = 0

    def __post_init__(self):
        if self.remaining is None:
            self.remaining = self.burst
