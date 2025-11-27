# Übungsblatt — Woche 03: Prioritäts‑Scheduling & SJF/SRT

**Lernziele**

- Den Unterschied zwischen non-preemptive SJF und preemptive SRT erklären können;
- Wissen, wie Prioritäts-Scheduling funktioniert und welche Probleme (Starvation, Priority Inversion) auftreten können;
- Einfache Scheduler-Klassen in Python implementieren (SjfScheduler, SrtScheduler) und testen;
- Metriken (response, waiting, turnaround) mit Simulatoren messen und Gantt-Diagramme interpretieren;
- Einfache Gegenmaßnahmen wie Aging implementieren und ihre Wirkung analysieren.

**Aufgaben**

1. Implementiere `StudentPriorityScheduler` in `src/week03/student/scheduler.py` (non-preemptive):
   - Wähle den Prozess mit der höchsten Priorität (niedrigere Zahl = höhere Priorität). Bei Gleichstand: kürzere verbleibende Zeit, dann niedrigere PID.
2. Implementiere optional `StudentSrtScheduler` (preemptive SRT):
   - Wähle stets den Prozess mit der geringsten verbleibenden Zeit.
3. Führe das Notebook `notebooks/week03_priority.ipynb` aus und vergleiche avg_wait für SJF (non-preemptive) und SRT (preemptive) auf dem Beispiel-Szenario.

**Dateien**
- Starter-Code: `src/week03/student/scheduler.py` (Stubs).
- Referenz: `src/week03/reference/scheduler.py`.
- Simulator: `src/week03/sim/simulator.py`.
- Notebook: `notebooks/week03_priority.ipynb`.
- Tests: `tests/test_student_week03.py`, `tests/test_priority_behavior.py`.

**Abgabe / Bewertung**
- Keine formale Abgabe. Die Implementierungen werden in der Übung besprochen. Tests dienen als Selbstcheck.
