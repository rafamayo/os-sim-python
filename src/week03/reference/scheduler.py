from typing import List, Optional
from common.process import Process

class PriorityScheduler:
    """Non-preemptive priority scheduler: chooses process with highest priority.
    Smaller numeric priority value = higher priority (e.g., 0 highest).
    In case of ties, choose the one with smallest remaining time, then lowest pid.
    """
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        best = min(processes, key=lambda p: (p.priority, p.remaining, p.pid))
        return best

class SjfScheduler:
    """Non-preemptive SJF: choose job with smallest service time (remaining).
    """
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        best = min(processes, key=lambda p: (p.remaining, p.arrival, p.pid))
        return best

class SrtScheduler:
    """Preemptive SRT (Shortest Remaining Time): at each decision point choose
    the process with smallest remaining time.
    """
    def schedule(self, processes: List[Process]) -> Optional[Process]:
        if not processes:
            return None
        best = min(processes, key=lambda p: (p.remaining, p.arrival, p.pid))
        return best
