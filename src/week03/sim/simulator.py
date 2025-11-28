import copy
import math
from typing import List, Tuple, Optional, Any
from common.process import Process
float_eps = 1e-12


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


def run_simulation_sjf(scheduler: Any, processes: List[Any]) -> List[Tuple[int, float, float]]:
    """
    Non-preemptive SJF simulation.

    Behaviour:
      - event-driven: advance to next arrival when no ready procs
      - when CPU free: select from ready the process with smallest service time
        (tie-breakers: burst, arrival, pid)
      - run the chosen process to completion (non-preemptive)
    Returns list of tuples (pid, waiting, turnaround) in completion order.
    """
    # defensive deepcopy so simulator doesn't mutate caller's objects
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready = []
    completed = []
    time = 0.0

    def push_arrivals_up_to(t: float):
        nonlocal procs, ready
        while procs and procs[0].arrival <= t:
            ready.append(procs.pop(0))

    while procs or ready:
        # bring arrivals that have arrived by `time`
        push_arrivals_up_to(time)

        # if nothing ready, jump to next arrival time
        if not ready:
            if procs:
                time = procs[0].arrival
                push_arrivals_up_to(time)
            else:
                break

        # choose smallest service time among ready (burst or remaining)
        # tie-break: burst (or remaining), then arrival, then pid for determinism
        def key_fn(p):
            # use 'remaining' if present (robustness), else fall back to burst
            svc = getattr(p, "remaining", None)
            if svc is None:
                svc = getattr(p, "burst", float('inf'))
            return (svc, getattr(p, "arrival", 0.0), getattr(p, "pid", 0))

        p = min(ready, key=key_fn)
        # remove chosen process from ready list (by identity/pid)
        try:
            ready.remove(p)
        except ValueError:
            ready = [r for r in ready if r.pid != p.pid]

        # determine start, waiting and run to completion
        start = time
        waiting = start - p.arrival
        exec_time = getattr(p, "remaining", None)
        if exec_time is None:
            exec_time = getattr(p, "burst", 0.0)
        # run to completion (non-preemptive)
        time += exec_time
        # mark as finished
        finish = time
        turnaround = finish - p.arrival
        # ensure consistency for callers expecting mutated Process (optional)
        p.remaining = 0.0
        completed.append((p.pid, waiting, turnaround))

    return completed


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
            turnaround = finish - p.arrival
            waiting = turnaround - p.burst
            completed.append((p.pid, waiting, turnaround))
        else:
            # preempted by next arrival; loop will add arrivals and scheduler will pick next
            pass
    return completed
