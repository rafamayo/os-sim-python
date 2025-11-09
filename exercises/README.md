## Übersicht (Woche für Woche)

| Woche | Thema (Kurz)                                   | Praktische Aufgaben (Kernauswahl)                                                                                                                     | Dateien / Artefakte (Studenten)                                                              |
| ----: | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
|     1 | Grundlagen: Scheduler & Ready‑Queue (FIFO)     | &bull; Implementiere `StudentFifoScheduler` in `src/student/schedule.py`. <br> &bull; Convoy‑Experiment (Notebook) — messe `avg_wait`/`avg_turn`.                        | &bull; `src/student/schedule.py`,<br> &bull; `src/sim/simulator.py`, <br> &bull; `notebooks/week01_scheduler_basics.ipynb` |
|     2 | Scheduler‑Strategien: Round‑Robin & Preemption | &bull; Implementiere `RoundRobinScheduler` (z.B. `src/student/round_robin.py`) oder erweitere die Harness für quantisiertes Scheduling; <br> &bull; vergleiche Metriken. | &bull; `src/student/round_robin.py`, <br> &bull; Notebook                                                       |
|     3 | Prioritäts‑Scheduling & SJF/SRT                | &bull; Implementiere einfache Prioritätsauswahl oder SJF (non‑preemptive) / SRT (preemptive). <br> &bull; Diskutiere Starvation.                                         | &bull; `src/student/priority_scheduler.py` (optional), <br> &bull; Tests                                        |
|     4 | Prozessmodell & Process Control Block (PCB)    | &bull; Entwerfe `ProcessControlBlock` (Zustände: NEW, READY, RUNNING, BLOCKED, TERMINATED) und integriere in die Harness.  | &bull; `src/student/pcb.py`, <br> &bull; Simulator‑Erweiterungen                                                |
|     5 | Kontextwechsel & Scheduling‑Overheads          | &bull; Simuliere Context‑Switch‑Kosten (Zeit/Overhead) und messe Effekte auf `turnaround`.                                                                   | &bull; Änderungen in `src/sim/simulator.py`, <br> &bull; Messskripts                                            |
|     6 | Interprozess‑Kommunikation (IPC)               | &bull; Implementiere Blocking Send/Receive (Pipes/Message Passing) und erstelle Producer/Consumer‑Szenarien.                                                 | &bull; `src/student/ipc.py`, <br> &bull; Notebook                                                               |
|     7 | Synchronisation: Mutex, Semaphoren             | &bull; Implementiere Locks / Semaphoren; <br> &bull; Demonstriere Race Conditions und Lösungen.                                                                          | &bull; `src/student/sync.py`, <br> &bull; Tests                                                                 |
|     8 | Threading vs. Prozessmodell                    | &bull; Simuliere Threads/leichtgewichtige Prozesse; <br> &bull; Vergleiche Shared Memory vs. Message Passing.                                                            | &bull; Notebooks, <br> &bull; kleine Implementierungen                                                          |
|     9 | Virtual Memory – Paging (Grundlagen)           | &bull; Implementiere Seitentabellen‑Skeleton, Page‑Table‑Lookup, <br> &bull; Visualisiere Page‑Faults.                                                                   | &bull; `src/student/vm.py`, <br> &bull; Notebook                                                                |
|    10 | Page Replacement Algorithmen                   | &bull; Implementiere FIFO, LRU, Clock; <br> &bull; Messe Hit/Miss‑Ratios für Workloads.                                                                                  | &bull; `src/student/paging/*.py`, <br> &bull; Tests, <br> &bull; Plots                                                      |
|    11 | Dateisystem – Inodes & File API                | &bull; Implementiere vereinfachte Inode‑Struktur und `open/read/write` Verhalten; <br> &bull; berechne Blockzugriffe.                                                    | &bull; `src/student/fs.py`, <br> &bull; Übungsblätter                                                           |
|    12 | Dateisystem – Directory & Allocation           | &bull; Vergleiche Allokationsstrategien (FAT/Extent/Indexed) und diskutiere Performance.                                                                     | &bull; `src/student/fs_alloc.py`                                                                    |
|    13 | I/O Scheduling & Device Model                  | &bull; Simuliere Disk‑Queue (FCFS, SSTF) und messe Durchsatz/Latenz; <br> &bull; Modelliere Gerätekosten.                                                                | &bull; `src/student/io.py`                                                                          |
|    14 | Sicherheit & Isolation (Überblick)             | &bull; Konzepte: Privilegien, Isolation, einfache Policy‑Checks; <br> &bull; Kleine Sandbox‑Übung.                                                                       | &bull; Notebooks, <br> &bull; kleine Implementierung                                                           |
|    15 | Abschlussprojekt & Integration                 | &bull; Integriere Scheduler + VM + FS + IPC in Mini‑OS‑Simulator; <br> &bull; Präsentationen/Demos.                                                                      | &bull; Projekt‑Repo/Branches, <br> &bull; Demo‑Notebooks    

---

## Format der Übungen / Ablauf / Abgabe

* **Dauer:** Jede Woche 90 min Theorie + 90 min Übung.
* **Arbeitsweise:** Studierende arbeiten an Starter‑Code in `src/student/` und benutzen `src/reference/` nur zur Demonstration.
* **Tests:** Öffentliche Tests in `tests/` dienen als Selbstcheck. Versteckte Tests / Bewertungs‑Suiten befinden sich in einem privaten Instructor‑Repo oder in einer geschützten CI‑Umgebung.
* **Abgabe:** In diesem Kurs gibt es (standardmäßig) keine formale Abgabe wöchentlich — die Implementationen werden im Tutorium/Übung besprochen. Für Projekt‑/Bewertungswochen (z. B. 15) kann eine Abgabe via GitHub‑Repo/Tag erfolgen.

---

## Hinweise zur Repository‑Organisation

* **Studenten‑Dateien:** `src/student/*` (hier implementieren Studierende).
* **Referenz/Demo:** `src/reference/*` (Instructor demos, nicht ändern).
* **Simulator‑Harness:** `src/sim/*` (gemeinsame Logik für alle Wochen).
* **Tests:** `tests/*` (sichtbare Tests).
* **Exercises/Sheets:** `exercises/weekNN/README.md` (Übungsblätter, expectations).
* **Docs:** `docs/weekNN/*` (technische Beschreibungen, Referenzen).
* **Instructor‑only:** `instructor/` (lösungen, hidden tests) — **nicht** in den öffentlichen Student‑Repo pushen.

---

## Bewertung & Kriterien (Kurz)

* Funktionalität (Tests grün) — 60% (Selbstcheck + besprochene Features).
* Code‑Qualität / Lesbarkeit / geeignete Tests — 20%.
* Teilnahme an Besprechungen, Mündliche Demo/Fragen — 20%.

(Anmerkung: exakte Gewichtung je nach Studiengang / Prüfungsordnung anpassen.)

---

## Tipp: Autoreload

* Debugging: Erklärung von `autoreload`‑Workflow für Jupyter (alternativ: Kernel‑Restart).







