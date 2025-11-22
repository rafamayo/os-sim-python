from typing import List, Optional
from common.process import Process

class StudentPriorityScheduler:
    """Student stub: implement non-preemptive priority scheduling.
    schedule(self, processes) should return the chosen Process instance.
    """
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        raise NotImplementedError("Implement StudentPriorityScheduler.schedule()")


class StudentSrtScheduler:
    """Student stub: implement preemptive SRT scheduling.
    schedule(self, processes) -> Process
    The simulator will call schedule repeatedly at event boundaries.
    """
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        raise NotImplementedError("Implement StudentSrtScheduler.schedule()")
