# Übungsblatt — Woche 01: Scheduler Basics (Python)

* **Kurs:** Betriebssysteme (OS-Simulator)
* **Dauer (empfohlen):** 90 Minuten Übungssitzung (+ Vor- und Nachbereitung)
* **Ort im Repo:** `exercises/week01/README.md`

---

## Lernziele

* Verstehen, was ein Scheduler tut (Ready-Queue, Auswahl des nächsten Prozesses).
* Prozesse mit `arrival` und `burst` modellieren und `remaining` nutzen.
* Eine einfache FIFO-Scheduler-Strategie in `src/week01/student/scheduler.py` implementieren.
* Eine kleine Simulations-Harness benutzen, um Scheduler miteinander zu vergleichen (Convoy-Experiment).
* Tests lokal ausführen und Notebooks interaktiv nutzen.

---

## Vorbereitung (vor der Übung)

1. Repository klonen: `git clone <REPO-URL>` und in den Projektordner wechseln.
2. Virtuelle Umgebung anlegen und aktivieren (siehe `docs/Projekt-Quickstart.md`).
3. Abhängigkeiten installieren:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt    # optional für JupyterLab / Dev-Tools
   ```
4. Empfohlen: editable install, damit `reference`/`student`-Module sauber importierbar sind:

   ```bash
   pip install -e .
   ```
5. Prüfe initial: `pytest tests/week01 -q` (soll die Referenz-smoke-tests laufen lassen).

---

## Wichtiger Hinweis zu den Quell-Dateien

* **Nicht verändern:** `src/week01/reference/scheduler.py` enthält die *instructor/reference* Implementierung (nur zur Demonstration). Bitte **ändere diese Datei nicht**.
* **Implementieren:** `src/week01/student/scheduler.py` ist als **Skeleton/Stub** vorgesehen — dort implementierst du `StudentFifoScheduler.schedule(processes)`. Die Aufgaben und die Tests beziehen sich auf diese Datei.

---

## Aufgaben (Schritt für Schritt)

### Aufgabe A — Orientierung & Demo (10–15 min)

1. Öffne das Notebook: `notebooks/week01_scheduler_basics.ipynb` (lokal in JupyterLab oder in Colab).
2. Führe die Demo-Zellen aus, die die Referenz-FIFO zeigen.
3. Lies die Hinweise in diesem Blatt und in den Docstrings der Student-Starterdatei.

### Aufgabe B — Implementiere `StudentFifoScheduler` (30–40 min)

1. Öffne `src/week01/student/scheduler.py`.
2. Implementiere die Methode:

   ```py
   class StudentFifoScheduler:
       def schedule(self, processes: List[Process]) -> Optional[Process]:
           ...
   ```

   Erwartetes Verhalten: gib das erste Element der `processes`-Liste zurück oder `None`, falls die Liste leer ist. (Die Simulation erwartet, dass dieselbe Objekt-Instanz zurückgegeben wird, die sich in der `ready`-Liste befindet.)
3. Führe die Tests:

   ```bash
   pytest tests/week01 -v -r a
   ```

   oder nur die relevanten Tests:

   ```bash
   pytest tests/week01/test_student_scheduler.py tests/week01/test_scheduler_metrics.py -q
   ```

### Aufgabe C — Convoy-Experiment (30–40 min)

1. Benutze die Simulations-Harness `run_simulation` (in `src/week01/sim/simulator.py`) mit folgendem Szenario:

   * P1: `arrival=0.0`, `burst=100.0`
   * P2: `arrival=0.1`, `burst=1.0`
   * P3: `arrival=0.2`, `burst=1.0`
2. Führe `run_simulation(FifoScheduler(), [p1,p2,p3])` aus und sammle `(pid, waiting, turnaround)`-Werte.
3. Berechne `avg_wait` und `avg_turn` und begründe, warum FIFO in diesem Szenario ungünstig ist (Convoy-Effekt).

---

## Tests (wichtig)

* **Student-API Test:** `tests/week01/test_student_scheduler.py` prüft, dass `StudentFifoScheduler` existiert und korrekt funktioniert (leere Liste → `None`, non-empty → erstes Element).
* **Convoy Metric Test:** `tests/week01/test_scheduler_metrics.py` führt das Convoy-Szenario auf der Referenz-FIFO aus und prüft, dass kurze Jobs deutlich warten müssen (robuste Assertion, kein exaktes Zahlen-Matching).
* Testlauf (empfohlen verbose):

  ```bash
  pytest tests/week01 -v -r a --tb=short
  ```

---

## Hinweise für Studierende / Troubleshooting

* **ImportError: No module named 'reference' / 'src'**

  * Stelle sicher, dass du im Projekt-Root arbeitest und die venv aktiv ist.
  * Führe `pip install -e .` aus, damit `reference` / `student` importierbar sind.
  * Alternativ temporär im Notebook:

    ```py
    import sys, os
    sys.path.append(os.path.abspath('.'))
    ```
* **Die Referenz darf nicht verändert werden.** Falls du etwas an der API ändern willst (z. B. Feldnamen), sprich vorher mit der Lehrperson — Tests und Notebooks erwarten die vorgegebenen Feldnamen (`pid`, `arrival`, `burst`, `remaining`, `priority`).
* **Wenn Tests fehlschlagen**, lies die Fehlermeldung (mit `-v --tb=short`); poste den Traceback in Issues/Forum oder bring ihn in die Sprechstunde.

---

## Akzeptanzkriterien / Abnahme (Selbsttest)

* `tests/week01/test_student_scheduler.py` und `tests/test_scheduler_metrics.py` laufen lokal grün.
* Notebook-Convoy-Zellen laufen ohne Fehler und zeigen erwartetes Verhalten (P2/P3 hohe waiting bei FIFO).
* `src/week01/student/scheduler.py` enthält keine Kopie der Referenz-Lösung (also: implementiert, aber nicht bereits vorimplementiert).

---

## Optional / Erweiterungen (Bonus)

* Instrumentiere den Scheduler so, dass er eine interne Zählung (`schedule_count`) führt.
* Implementiere `RoundRobinScheduler` und vergleiche Metriken grafisch (Notebook + matplotlib).
* Erzeuge deterministische Tests für mehrere Workloads und vergleiche mittlere Wartezeit über Strategien.

---

## Wo finden die relevanten Dateien?

* Referenz: `src/week01/reference/scheduler.py` (nicht editieren).
* Student Skeleton: `src/week01/student/scheduler.py` (hier implementieren).
* Simulator: `src/week01/sim/simulator.py`.
* Tests: `tests/week01/test_student_scheduler.py`, `tests/test_scheduler_metrics.py`.
* Notebook: `notebooks/week01_scheduler_basics.ipynb`.




