from typing import List, Tuple
from common.process import Process

def run_simulation(scheduler, processes: List[Process]):
    """Run a simple discrete simulation returning list of (pid, waiting, turnaround).

    Scheduler must implement schedule(ready_list) and return a Process or None.
    FIFO semantics: chosen process runs to completion (remaining -> 0).
    """
    time = 0.0
    ready: List[Process] = []
    completed: List[Tuple[int, float, float]] = []
    procs = sorted(processes, key=lambda p: p.arrival)

    while procs or ready:
        # Bring arrived procs into ready queue
        while procs and procs[0].arrival <= time:
            ready.append(procs.pop(0))
        if not ready:
            # No ready process: advance time to next arrival
            time = procs[0].arrival
            continue
        p = scheduler.schedule(ready)
        if p is None:
            # Scheduler did not choose anyone - advance time
            time = procs[0].arrival
            continue
        # Run to completion (FIFO semantics)
        try:
            ready.remove(p)
        except ValueError:
            # If scheduler returned a Process not in ready (defensive), skip
            continue
        start = time
        time += p.remaining
        p.remaining = 0
        finish = time
        turnaround = finish - p.arrival
        waiting = start - p.arrival
        completed.append((p.pid, waiting, turnaround))
    return completed
