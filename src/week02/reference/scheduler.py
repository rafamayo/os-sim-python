from typing import List, Optional
from common.process import Process

class FifoScheduler:
    """Simple FIFO scheduler: returns first process in ready queue or None."""
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        return processes[0]

class RoundRobinScheduler:
    """Reference Round-Robin scheduler with internal pointer."""
    def __init__(self, quantum: float = 1.0):
        self.quantum = quantum
        self._next_index = 0

    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        idx = self._next_index % len(processes)
        p = processes[idx]
        # advance pointer for next scheduling call
        self._next_index = (idx + 1) % max(1, len(processes))
        return p
