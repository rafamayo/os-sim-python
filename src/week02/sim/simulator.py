import copy
from typing import List, Tuple, Dict, Optional, Any
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


def run_simulation_rr(scheduler: Any, processes: List[Any]) -> List[Tuple[int, float, float, Optional[float]]]:
    """
    Nicht-instrumentierte Round-Robin-Simulation (kein Context-Switch-Overhead).
    Returns: list of tuples (pid, waiting, turnaround, response) SORTED BY PID.

    - waiting = turnaround - burst
    - turnaround = finish - arrival
    - response = first_start - arrival
    """
    float_eps = 1e-12
    time = 0.0
    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready = deque()
    completed = []  # completion tuples in completion order
    first_start = {}  # pid -> first time the process got CPU (absolute time)

    # Hilfsfunktion: Ankünfte bis Zeit t in ready verschieben (in arrival order)
    def push_arrivals_up_to(t: float):
        nonlocal procs, ready
        while procs and procs[0].arrival <= t:
            ready.append(procs.pop(0))

    quantum = getattr(scheduler, 'quantum', 1.0)

    # Hauptschleife
    while procs or ready:
        # neue Ankünfte hinzufügen
        push_arrivals_up_to(time)

        # falls keine Ready-Prozesse, auf nächste Ankunft springen
        if not ready:
            if procs:
                time = procs[0].arrival
                push_arrivals_up_to(time)
            else:
                break

        # klassisches RR: erstes Element aus der Queue
        p = ready.popleft()

        # first_start (absolute time) falls erste Ausführung
        if p.pid not in first_start:
            first_start[p.pid] = time

        # exec_time: genau ein Quantum oder Restdauer
        exec_time = min(float(quantum), float(p.remaining))

        # ausführen
        p.remaining -= exec_time
        time += exec_time

        # sofort Ankünfte die während [start,time] gekommen sind hinzufügen,
        # damit sie vor dem wieder eingefügten p in der ready-Queue stehen
        push_arrivals_up_to(time)

        # Prozess fertig?
        if p.remaining <= float_eps:
            finish = time
            arrival = p.arrival
            burst = p.burst
            turnaround = finish - arrival
            waiting = turnaround - burst
            # response: convert absolute first_start to relative time
            response_abs = first_start.get(p.pid, None)
            response = (response_abs - arrival) if (response_abs is not None) else None
            completed.append((p.pid, waiting, turnaround, response))
        else:
            # nicht fertig: ans Ende der ready-Queue
            ready.append(p)

    # --- SORTIERUNG nach PID für stabile Ausgabe ---
    completed_sorted = sorted(completed, key=lambda x: x[0])  # sort by pid
    return completed_sorted


# --- student_version_run_simulation_rr_instrumented.py ---
import copy
from collections import deque
from typing import List, Tuple, Dict, Optional, Any

def run_simulation_rr_instrumented(
    scheduler: Any,
    processes: List[Any],
    context_switch_time: float = 0.0,
    record_switch_segments: bool = False,
    float_eps: float = 1e-12
) -> Dict[str, Any]:
    """
    Vereinfachter, didaktischer Round-Robin-Simulator (STUDENT VERSION).
    Eure Aufgabe: Ergänzt die markierte Stelle weiter unten (<<STUDENT CODE>>).
    Hinweise stehen direkt in der markierten Stelle.

    WICHTIG: scheduler.quantum liefert die Länge eines Zeitscheibenslots.
    Diese Implementierung verwendet eine ready-Queue (deque) und führt klassisches RR aus:
      p = ready.popleft(); führe p für min(quantum, p.remaining); danach reinserte p falls nicht fertig.
    """

    procs = sorted([copy.deepcopy(p) for p in processes], key=lambda p: p.arrival)
    ready = deque()
    timeline: List[Tuple] = []
    completed: List[Tuple[int, float, float, Optional[float]]] = []
    per_process: Dict[int, Dict[str, Optional[float]]] = {}

    # initial per_process
    for p in procs:
        per_process[p.pid] = {
            'arrival': float(p.arrival),
            'burst': float(p.burst),
            'total_run': 0.0,
            'first_start': None,
            'finish': None
        }

    time = 0.0
    quantum = getattr(scheduler, 'quantum', 1.0)
    context_switches = 0

    def record_exec_segment(pid: int, start: float, duration: float):
        end = start + duration
        timeline.append((pid, start, end))
        per_process[pid]['total_run'] += duration
        if per_process[pid]['first_start'] is None:
            per_process[pid]['first_start'] = start
        return end

    def record_cs_segment(start: float, duration: float):
        end = start + duration
        if record_switch_segments:
            timeline.append(('cs', start, end))
        return end

    # Hilfsfunktion: Ankünfte bis Zeit t in ready einfügen
    def push_arrivals_up_to(t: float):
        nonlocal procs, ready
        while procs and procs[0].arrival <= t:
            arriving = procs.pop(0)
            ready.append(arriving)
            if arriving.pid not in per_process:
                per_process[arriving.pid] = {
                    'arrival': float(arriving.arrival),
                    'burst': float(arriving.burst),
                    'total_run': 0.0,
                    'first_start': None,
                    'finish': None
                }

    # ---------- Hauptschleife ----------
    while procs or ready:
        push_arrivals_up_to(time)

        if not ready:
            if procs:
                time = procs[0].arrival
                push_arrivals_up_to(time)
            else:
                break

        # klassisches RR: nimm vorderstes Element
        p = ready.popleft()

        # berechne exec_time
        exec_time = min(float(quantum), float(p.remaining))
        start = time
        end = record_exec_segment(p.pid, start, exec_time)
        time = end
        p.remaining -= exec_time

        # ===============================
        # << STUDENT CODE: WICHTIGE Lücke >>
        #
        # Ziel: Ergänzt hier den Code, der nach dem Ausführen
        #       des Quants passieren muss. Konkrete Anforderungen:
        #
        # 1) Füge alle Prozesse ein, die *während* [start, end] angekommen sind,
        #    in die ready-Queue (in Ankunftsreihenfolge).
        #    Tipp: benutze push_arrivals_up_to(time) — aber achtet auf die Reihenfolge!
        #
        # 2) Falls p noch nicht fertig ist (p.remaining > float_eps), dann muss p
        #    ans Ende von ready angefügt werden. WICHTIG: Die Neuankömmlinge,
        #    die während des Quants eingetroffen sind, müssen *vor* p kommen.
        #
        # 3) Wenn das Quantum abgelaufen ist (d.h. exec_time == quantum) UND der
        #    Prozess nicht fertig ist, so muss ein Context Switch modelliert werden:
        #        if context_switch_time > 0.0: time += context_switch_time
        #    (Optional: falls record_switch_segments True ist, zeichnet den CS-Segment).
        #    Hinweis: Auch wenn danach nur p im ready steht, soll trotzdem ein CS stattfinden.
        #
        # 4) Wenn der Prozess fertig ist (p.remaining <= float_eps), dann:
        #       - setze per_process[p.pid]['finish'] = time
        #       - berechne turnaround/waiting/response und füge in completed ein
        #
        # Kleiner Tipp: Überlegt Euch die Reihenfolge:
        #    (a) arrival handling,
        #    (b) reinsertion oder removal von p,
        #    (c) context switch time addition
        #
        # Implementiert hierzu 6-12 Codezeilen.
        # ===============================
        # >>>>> HIER EUREN CODE EINFÜGEN <<<<<
        raise NotImplementedError("Student: Ergänzt hier arrivals/reinsertion/context-switch handling.")
        # ===============================
        # Ende der Lücke
        # -------------------------------

    # format results
    completed_sorted = sorted(completed, key=lambda x: x[0])
    results: List[Tuple[int, float, float, Optional[float]]] = []
    for pid, wait, turn, resp in completed_sorted:
        if resp is None and per_process[pid]['first_start'] is not None:
            resp = per_process[pid]['first_start'] - per_process[pid]['arrival']
        results.append((pid, wait, turn, resp))

    return {
        'results': results,
        'timeline': timeline,
        'context_switches': context_switches,
        'per_process': per_process
    }
