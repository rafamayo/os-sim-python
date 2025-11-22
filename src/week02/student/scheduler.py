from typing import List, Optional
from common.process import Process

class StudentRoundRobinScheduler:
    """Student skeleton for Round-Robin scheduler.

    Implement `schedule(self, processes)` to return an element from `processes`
    using round-robin selection. The simulation harness will call schedule()
    repeatedly for each quantum; your scheduler should maintain any required
    internal state (pointer/index) so that the next call selects the subsequent
    ready process. Return None if `processes` is empty.

    IMPORTANT: return the exact Process instance from the `processes` list,
    do NOT create or return a new Process object.
    """
    def __init__(self, quantum: float = 1.0):
        self.quantum = quantum
        # student should maintain an index pointer; initialize to 0
        self._next_index = 0

    def schedule(self, processes: List[Process]) -> Optional[Process]:
        # TODO: implement round-robin selection logic
        raise NotImplementedError("Implement StudentRoundRobinScheduler.schedule()")
