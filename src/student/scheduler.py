"""Student scheduler module.

Implement a scheduling policy here. For Week 1, implement a FIFO scheduler
by providing a class `StudentFifoScheduler` with a `schedule(processes)` method.
"""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Process:
    pid: int
    priority: int = 0

class StudentFifoScheduler:
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        # TODO: implement scheduling logic
        # For now, naive placeholder:
        if not processes:
            return None
        return processes[0]
