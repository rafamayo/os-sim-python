"""Reference FIFO scheduler for demos.

Provides a minimal Process dataclass and a FifoScheduler implementation
used for demo purposes and CI smoke tests.
"""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Process:
    pid: int
    priority: int = 0

class FifoScheduler:
    """Simple FIFO scheduler: returns first process in ready queue or None."""
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        return processes[0]
