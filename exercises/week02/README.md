# Übungsblatt — Woche 02: Scheduler‑Strategien: Round‑Robin & Preemption

**Lernziele**
- Verstehen, wie Round‑Robin (RR) mit quantisierten Zeitscheiben arbeitet.
- Implementieren eines einfachen RR‑Schedulers und Vergleich mit FIFO.
- Verstehen, wie Preemption die Reaktionszeit (waiting) und Turnaround beeinflusst.

**Aufgaben**
1. Implementiere die Klasse `StudentRoundRobinScheduler` in `src/wwek02/student/scheduler.py`.
   - Die Methode `schedule(self, processes)` soll ein Element aus `processes` zurückgeben
     entsprechend der Round‑Robin‑Auswahl (Pointer/Index), oder `None`, falls `processes` leer ist.
   - Der Konstruktor akzeptiert ein `quantum` Argument (Standard 1.0) und die Klasse soll
     **intern den Index für die nächste Auswahl verwalten**.
2. Führe das Convoy‑Experiment (gleiches Szenario wie Woche 1) mit der mitgelieferten Simulator‑Harness
   aus: `sim/week02/simulator.py`. Vergleiche die Metriken `avg_wait` und `avg_turn` zwischen FIFO und RR.
3. Optional: experimentiere mit verschiedenen `quantum`‑Werten (0.5, 1.0, 2.0) und beobachte die Auswirkungen.

**Dateien / Hinweise**
- Starter‑Code liegt in `src/week02/` (siehe `src/week02/student/scheduler.py` — implementiere dort).
- Notebooks: `notebooks/week02_rr.ipynb` demonstriert die Nutzung der Harness.
- Tests: `tests/week02/test_student_rr.py` und `tests/week02/test_rr_metrics.py`.

**Abgabe / Bewertung**
- Keine formale Abgabe; Implementationen werden in der Übung besprochen. Tests dienen als Selbstcheck.
