# Week 04 — Prozessmodell & Process Control Block (PCB)

**Kurz:** In dieser Woche entwerfen und benutzen Sie eine einfache Implementierung des Process Control Block (PCB). Ziel ist, das Zustandsmodell (NEW, READY, RUNNING, BLOCKED, TERMINATED) kennenzulernen und zu üben, wie Prozesse in der Simulation mittels PCBs verwaltet werden.

---

## Lernziele

* Verstehen, welche Informationen ein PCB enthält und warum es wichtig ist.
* Zustandsübergänge eines Prozesses modellieren und nachvollziehen.
* PCB in die Simulation integrieren (Anlegen, State-Updates bei Dispatch/Stop/Block).
* Mit einfachen Tests und einem kleinen Notebook die Funktionalität validieren.

---

## Dateien (im Repo / in diesem Exercise-Paket)

* `src/student/pcb.py`

  * **Studierenden-Datei**: enthält `ProcessControlBlock` und `ProcessState` Enum (Implementierungsvorlage).
* `src/sim/pcb_harness.py`

  * Helferfunktionen: `create_pcb_from_process`, `attach_pcb_to_process`, `on_dispatch_start/stop`, `on_block/unblock`.
* `tests/test_pcb.py`

  * Kleine PyTest-Tests, die die grundlegende PCB-API prüfen.
* `run_pcb_demo.ipynb`

  * Kurzes Demo-Notebook, das zeigt, wie ein `Process` in ein `PCB` umgewandelt wird und wie Felder bei Dispatch verändert werden.

> **Hinweis:** Die Studierenden sollten primär `src/student/pcb.py` bearbeiten. Die anderen Dateien sind Hilfs-/Instructor-Artefakte.

---

## Aufgaben (Studenten-Version)

1. **Tests ausführen (Schnellcheck):**

   ```bash
   pytest -q ./tests/week04
   ```

   Die Tests geben erstes Feedback zur API-Konformität.

2. **Implementierung prüfen / erweitern:**

   * Öffnen Sie `src/week04/student/pcb.py`.
   * Stellen Sie sicher, dass `ProcessControlBlock` die Felder besitzt: `pid, state, arrival, burst, remaining, priority, registers, fd_table`.
   * Methoden: `set_state(new_state)`, `is_terminated()`, `snapshot()`.
   * Achten Sie auf eine sinnvolle Initialisierung (z. B. `remaining = burst` falls None).

3. **Demo-Notebook ausführen:**

   * Starten Sie JupyterLab und öffnen Sie `week04_run_pcb_demo.ipynb`.
   * Führen Sie die Zellen aus und beobachten Sie die Statusänderungen.

4. *(Optional, fortgeschritten)* Integration in Simulator:

   * Erzeugen Sie PCBs für alle Prozesse im Simulator (`attach_pcb_to_process`) und verwenden Sie `on_dispatch_start/stop` an den passenden Stellen (Dispatcher / End-of-quantum / Completion).
   * Ziel: die Simulation soll nun die PCB-Objekte pflegen (Zustandswechsel sichtbar in `pcb.snapshot()`).

---

## Didaktische Hinweise / Tipps

* **Warum `set_state()` benutzen?**

  * Alle State-Änderungen laufen über diese Methode. Damit können wir später Logging, Validierung oder Hooks zentral integrieren.
* **Fehlerquelle:** Versuchen Sie nicht, nach `TERMINATED` den State zu ändern — `set_state` sollte hier eine Exception werfen.
* **Snapshot:** `snapshot()` sollte JSON-serialisierbare Informationen zurückgeben (nützlich für Logging & Tests).

---

## Bewertung / Abgabe (Empfehlung)

* Hauptkriterium: Tests bestehen und `snapshot()` sinnvolle Werte liefert.
* Optional: Kurze Demo im Seminar zeigen (z. B. PCB-Inhalte vor/nach Dispatch).

---

## Erwartete Kommandos während der Arbeit

* Tests ausführen:

  ```bash
  pytest -q tests/test_pcb.py
  ```
* Notebook starten:

  ```bash
  jupyter lab run_pcb_demo.ipynb
  ```
