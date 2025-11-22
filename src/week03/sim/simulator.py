import copy
import math
from typing import List, Tuple, Optional
from common.process import Process

def run_simulation_priority(scheduler, processes: List[Process]) -> List[Tuple[int, float, float]]:
    """Non-preemptive simulation where scheduler selects next job to run to completion."""
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
            time = procs[0].arrival if procs else time
            continue
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


def run_simulation_sjf(scheduler, processes: List[Process]) -> List[Tuple[int, float, float]]:
    """Non-preemptive SJF simulation (alias to priority-runner behavior)
    """
    return run_simulation_priority(scheduler, processes)


def run_simulation_srt(scheduler, processes: List[Process]) -> List[Tuple[int, float, float]]:
    """Preemptive SRT simulation. The scheduler is called at each event boundary
    (arrivals or completions). We run the chosen process until the next arrival
    or until it completes, whichever comes first.
    """
    time = 0.0
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready: List[Process] = []
    completed = []
    first_start = {}
    INF = math.inf

    while procs or ready:
        while procs and procs[0].arrival <= time:
            ready.append(procs.pop(0))
        if not ready:
            time = procs[0].arrival
            continue
        p = scheduler.schedule(ready)
        if p is None:
            time = procs[0].arrival if procs else time
            continue
        t_next_arrival = procs[0].arrival - time if procs else INF
        run_for = min(p.remaining, t_next_arrival)
        if p.pid not in first_start:
            first_start[p.pid] = time
        p.remaining -= run_for
        time += run_for
        if p.remaining <= 0:
            try:
                ready.remove(p)
            except ValueError:
                ready = [r for r in ready if r.pid != p.pid]
            finish = time
            waiting = first_start[p.pid] - p.arrival
            turnaround = finish - p.arrival
            completed.append((p.pid, waiting, turnaround))
        else:
            # preempted by next arrival; loop will add arrivals and scheduler will pick next
            pass
    return completed
