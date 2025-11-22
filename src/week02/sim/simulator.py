import copy
from typing import List, Tuple, Optional
from common.process import Process

def run_simulation_fifo(scheduler, processes: List[Process]) -> List[Tuple[int, float, float]]:
    """Non-preemptive FIFO-style simulation: scheduler chooses a process which runs to completion."""
    time = 0.0
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready: List[Process] = []
    completed = []

    while procs or ready:
        while procs and procs[0].arrival <= time:
            ready.append(procs.pop(0))
        if not ready:
            time = procs[0].arrival
            continue
        p = scheduler.schedule(ready)
        if p is None:
            time = procs[0].arrival
            continue
        # remove chosen process (by identity/pid)
        try:
            ready.remove(p)
        except ValueError:
            ready = [r for r in ready if r.pid != p.pid]
        start = time
        time += p.remaining
        p.remaining = 0
        finish = time
        waiting = start - p.arrival
        turnaround = finish - p.arrival
        completed.append((p.pid, waiting, turnaround))
    return completed

def run_simulation_rr(scheduler, processes: List[Process]) -> List[Tuple[int, float, float]]:
    """Preemptive Round-Robin simulation using scheduler.quantum for time slices."""
    time = 0.0
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready: List[Process] = []
    completed = []
    first_start = {}

    while procs or ready:
        while procs and procs[0].arrival <= time:
            ready.append(procs.pop(0))
        if not ready:
            time = procs[0].arrival
            continue
        p = scheduler.schedule(ready)
        if p is None:
            # If scheduler returns None, fast-forward
            if procs:
                time = procs[0].arrival
            else:
                break
            continue
        # run for one quantum or until remaining finished
        exec_time = min(getattr(scheduler, 'quantum', 1.0), p.remaining)
        if p.pid not in first_start:
            first_start[p.pid] = time
        p.remaining -= exec_time
        time += exec_time
        # bring any newly arrived procs into ready at loop start (they will be appended)
        if p.remaining <= 0:
            # finished
            try:
                ready.remove(p)
            except ValueError:
                ready = [r for r in ready if r.pid != p.pid]
            finish = time
            waiting = first_start[p.pid] - p.arrival
            turnaround = finish - p.arrival
            completed.append((p.pid, waiting, turnaround))
        else:
            # time slice ended - rotate p to end of ready queue
            try:
                ready.remove(p)
            except ValueError:
                ready = [r for r in ready if r.pid != p.pid]
            ready.append(p)
    return completed
