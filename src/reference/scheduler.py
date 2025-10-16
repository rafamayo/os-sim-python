from dataclasses import dataclass, field
from typing import List, Optional

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

class FifoScheduler:
    """Simple FIFO scheduler: returns first process in ready queue or None."""
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        return processes[0]
