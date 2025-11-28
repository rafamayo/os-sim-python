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


"""
Student stub for run_simulation_srt (preemptive SRT)

Task for students (didactic):
Fill the marked section marked with ``STUDENT TASK``. The missing code must
handle reinserting a *preempted* process into the ready queue so that any
processes that arrived *during* the just-executed time interval appear *before*
the preempted process in the ready queue.

This is a small, focused exercise that forces students to reason about:
 - event-driven simulation (arrivals during a time slice),
 - correct ordering of the ready queue after preemption,
 - not duplicating arrivals.

The rest of the simulator is provided — students should only change the
marked section. Keep the function API identical.

Instructor notes are included at the end of the file.
"""

from typing import List, Tuple
import copy
import math

# The Process dataclass is expected to be provided by the course code base.
# It must have at least: pid, arrival, burst, remaining
# Example:
# @dataclass
# class Process:
#     pid: int
#     arrival: float
#     burst: float
#     remaining: float = None
#     def __post_init__(self):
#         if self.remaining is None:
#             self.remaining = self.burst


def run_simulation_srt(scheduler, processes: List['Process']) -> List[Tuple[int, float, float]]:
    """Preemptive SRT simulation.

    Behavior (provided):
      - event-driven: advance to next arrival when no ready procs
      - scheduler.schedule(ready) is called to pick the process to run
      - we run the chosen process until next arrival or until it completes
      - if preempted by arrivals, the process must be reinserted into ready

    STUDENT TASK: implement the reinsertion of a preempted process so that
    *processes that arrived during the run* are placed before the preempted
    process in the ready queue. To do so, you will need to move arrivals that
    happened during the just-executed interval from `procs` into `ready` and
    then append the preempted process.

    IMPORTANT: do not forget that arrivals must not be duplicated. If you
    decide to pop arrivals now, the top-of-loop arrival handling must not add
    them again (this implementation is compatible with popping them here).
    """

    time = 0.0
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready: List['Process'] = []
    completed = []
    first_start = {}
    INF = math.inf

    while procs or ready:
        # bring any processes that already arrived
        while procs and procs[0].arrival <= time:
            ready.append(procs.pop(0))

        if not ready:
            # fast-forward to next arrival
            time = procs[0].arrival
            continue

        # ask scheduler which process to run (should return one of `ready`)
        p = scheduler.schedule(ready)
        if p is None:
            # no decision -> jump to next arrival
            time = procs[0].arrival if procs else time
            continue

        # time until next arrival (relative to current time)
        t_next_arrival = procs[0].arrival - time if procs else INF
        # we will run for at most the remaining time of p or until the next arrival
        run_for = min(p.remaining, t_next_arrival)

        # mark first start for response-time computation
        if p.pid not in first_start:
            first_start[p.pid] = time

        # execute
        p.remaining -= run_for
        start_time = time
        time += run_for

        if p.remaining <= 0:
            # p finished during this interval
            try:
                ready.remove(p)
            except ValueError:
                # if identity mismatch, filter by pid
                ready = [r for r in ready if r.pid != p.pid]
            finish = time
            turnaround = finish - p.arrival
            waiting = turnaround - p.burst
            completed.append((p.pid, waiting, turnaround))
        else:
            # --- STUDENT TASK START ---
            # Reinsertion on preemption
            # When p was preempted (because a new arrival occurred), we must ensure
            # that the processes that arrived during (start_time, time] are placed
            # before `p` in the ready queue.
            #
            # A correct approach (one of several) is:
            #  1. Move all processes from `procs` whose arrival <= current `time`
            #     into the `ready` list now (pop them from `procs` and append to
            #     `ready`). These are exactly the arrivals that happened during
            #     the just-executed interval.
            #  2. Append the preempted process `p` to `ready` so that the newly
            #     arrived processes are ahead of `p` in the queue.
            #
            # NOTE for students: do _not_ simply do `ready.append(p)` and leave the
            # arrivals to be appended at the top of the next loop iteration —
            # that would place `p` before arrivals. Instead, collect the arrivals
            # now and then append `p`.
            #
            # Implement this behavior in the section below.

            # ====== YOUR CODE (STUDENT) ======
            # Replace the NotImplementedError with code that pushes arrivals and
            # reinserts the preempted process in the correct order.
            raise NotImplementedError("Student: implement reinsertion of preempted process here")
            # ====== END STUDENT CODE ======

            # --- STUDENT TASK END ---

    return completed


def run_simulation_srt_instrumented(scheduler: Any, processes: List[Any],
                                        context_switch_time: float = 0.0,
                                        record_cs_segments: bool = True) -> Dict[str, Any]:
    """Instrumented preemptive SRT simulator.

    Parameters
    ----------
    scheduler: object with schedule(ready) method. Should return a Process instance from `ready`
    processes: list of Process-like objects (pid, arrival, burst, remaining optional)
    context_switch_time: float seconds added whenever a context switch happens
    record_cs_segments: if True, cs segments are recorded in timeline as ('cs', start, end)

    Returns
    -------
    dict with keys 'timeline', 'per_process', 'results', 'context_switches'
    """
    INF = math.inf
    time = 0.0
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready: List[Any] = []
    timeline: List[Tuple[Any, float, float]] = []
    per_process: Dict[int, Dict[str, Any]] = {}
    context_switches = 0

    # initialize per_process info
    for p in procs:
        per_process[p.pid] = {
            "arrival": p.arrival,
            "burst": getattr(p, "burst", getattr(p, "remaining", 0.0)),
            "total_run": 0.0,
            "first_start": None,
            "finish": None,
        }

    def push_arrivals_up_to(t: float):
        nonlocal procs, ready
        while procs and procs[0].arrival <= t:
            ready.append(procs.pop(0))

    # helper to close last timeline segment for pid with end time
    def close_last_segment(pid_or_cs, end_time):
        if timeline and timeline[-1][0] == pid_or_cs and timeline[-1][2] is None:
            timeline[-1] = (timeline[-1][0], timeline[-1][1], end_time)

    current: Optional[Any] = None

    while procs or ready or current:
        # bring arrivals up to current time
        push_arrivals_up_to(time)

        # pick next process if none currently running
        if current is None:
            if not ready:
                # advance to next arrival if any
                if procs:
                    time = procs[0].arrival
                    push_arrivals_up_to(time)
                else:
                    break
            # ask scheduler for next process
            try:
                cand = scheduler.schedule(ready)
            except Exception:
                cand = None
            # interpret candidate
            chosen = None
            if cand is None:
                # fallback: pick minimal remaining (deterministic)
                if ready:
                    chosen = min(ready, key=lambda r: (getattr(r, "remaining", getattr(r, "burst", math.inf)), r.arrival, r.pid))
            else:
                # scheduler may return a pid or a Process instance
                if isinstance(cand, int):
                    found = [r for r in ready if getattr(r, "pid", None) == cand]
                    chosen = found[0] if found else None
                else:
                    matches = [r for r in ready if getattr(r, "pid", None) == getattr(cand, "pid", None)]
                    chosen = matches[0] if matches else None
                if chosen is None and ready:
                    # scheduler returned something unexpected -> fallback
                    chosen = min(ready, key=lambda r: (getattr(r, "remaining", getattr(r, "burst", math.inf)), r.arrival, r.pid))
            if chosen is None:
                # nothing to run
                continue
            # remove chosen from ready
            try:
                ready.remove(chosen)
            except ValueError:
                ready = [r for r in ready if r.pid != chosen.pid]

            # start chosen
            current = chosen
            if per_process[current.pid]["first_start"] is None:
                per_process[current.pid]["first_start"] = time
            # open timeline segment for this pid (end unknown)
            timeline.append((current.pid, time, None))
            # continue to execution phase below

        # determine time until next arrival
        next_arrival = procs[0].arrival if procs else None
        time_to_next_arrival = (next_arrival - time) if next_arrival is not None else INF
        exec_time = min(getattr(current, "remaining", getattr(current, "burst", 0.0)), time_to_next_arrival)

        if exec_time <= 0:
            # if next arrival is at current time, loop to push arrivals
            if procs and procs[0].arrival <= time + float_eps:
                push_arrivals_up_to(time)
                continue
            else:
                # nothing to do
                break

        # run current for exec_time
        current.remaining = getattr(current, "remaining", getattr(current, "burst", 0.0)) - exec_time
        per_process[current.pid]["total_run"] += exec_time
        time += exec_time

        # After running: either current finished, or preempted by arrival
        if current.remaining <= float_eps:
            # finish current
            close_last_segment(current.pid, time)
            per_process[current.pid]["finish"] = time
            # context switch may occur before next process runs (model it)
            if context_switch_time > 0.0 and (ready or procs):
                # record a cs segment
                if record_cs_segments:
                    timeline.append(('cs', time, None))
                time += context_switch_time
                if record_cs_segments:
                    # close cs segment
                    close_last_segment('cs', time)
                context_switches += 1
            current = None
            continue
        else:
            # preempted by arrival(s)
            # Close the running segment for current now (we'll reopen when it runs again)
            close_last_segment(current.pid, time)

            # --- Reinsertion & arrival handling (instructor: fully implemented) ---
            # Move any arrivals that happened during the execution into ready now,
            # and ensure they appear before the preempted process in the ready list.
            while procs and procs[0].arrival <= time:
                ready.append(procs.pop(0))

            # Append the preempted process so that newly arrived procs are before it
            ready.append(current)
            current = None

            # model a context switch before the next process runs (even if the next
            # process is the same, we count dispatch overhead)
            if context_switch_time > 0.0:
                if record_cs_segments:
                    timeline.append(('cs', time, None))
                time += context_switch_time
                if record_cs_segments:
                    close_last_segment('cs', time)
                context_switches += 1
            # loop continues, scheduler will pick next process
            continue

    # Build results: waiting, turnaround, response
    results = []
    for pid, info in per_process.items():
        arrival = info["arrival"]
        burst = info["burst"]
        finish = info["finish"]
        first_start = info["first_start"]
        turnaround = None if finish is None else finish - arrival
        waiting = None if turnaround is None else turnaround - burst
        response = None if first_start is None else first_start - arrival
        results.append((pid, waiting, turnaround, response))

    # sort results by pid for deterministic output
    results.sort(key=lambda x: x[0])

    return {
        "timeline": timeline,
        "per_process": per_process,
        "results": results,
        "context_switches": context_switches
    }
