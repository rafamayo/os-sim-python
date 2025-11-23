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


class StudentFifoScheduler:
    """
    TODO: Implement the FIFO scheduling policy.

    - schedule(self, processes: List[Process]) -> Optional[Process]
      should return the first element from the ready list (or None).
    - Do NOT modify the simulation harness -- it expects a Process object
      that is present in the 'processes' list.
    """
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        # Students: replace the following placeholder with your implementation.
        raise NotImplementedError("Implement StudentFifoScheduler.schedule()")
    
