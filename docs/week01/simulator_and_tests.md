# Referenz: `simulator.py` und Test‑Infrastruktur (Week 01)

Diese Referenzdokumentation erklärt die Simulations‑Harness `src/sim/simulator.py`, die getesteten Erwartungen und die Test‑Organisation für Woche 01. Sie ist als Nachschlagewerk für Studierende gedacht: welche API‑Verträge gelten, wie man Experimente ausführt, wie man sinnvolle Tests schreibt und wie man typische Fehler diagnostiziert.

---

## 1. Ziel dieser Dokumentation

* Beschreibe die **Process**‑Datenstruktur und Erwartungen an ihre Felder.
* Definiere die **Scheduler‑API** (was müssen Scheduler‑Klassen bereitstellen?).
* Erkläre die **run_simulation**‑Semantik: Annahmen, Datenfluss, Output.
* Beschreibe die **Testdateien**: welche Tests gibt es, was prüfen sie, wie laufen sie.
* Beispiele, Debugging‑Tipps und Hinweise, wie man eigene Tests ergänzt.

---

## 2. Wo die Dateien liegen (Konvention)

* `src/reference/scheduler.py` — Instructor/Referenzimplementierung (dürfen Studierende nicht verändern).
* `src/student/scheduler.py` — Student‑Starterdatei (hier implementieren Studierende).
* `src/sim/simulator.py` — Simulations‑Harness (run_simulation).
* `tests/test_student_scheduler.py` — API/Unit‑Tests für die Student‑Implementierung (existenz + simples Verhalten).
* `tests/test_scheduler_metrics.py` — Beispiel‑Szenario (Convoy) und Metriken.
* `docs/` — Dokumentation (diese Datei).

---

## 3. `Process` Dataclass — Felder & Bedeutung

Die `Process`‑Klasse modelliert einen Prozess in der Simulation. Erwartete Felder:

```py
@dataclass
class Process:
    pid: int           # eindeutige Prozess-ID
    arrival: float     # Ankunftszeit im System (z. B. in Zeiteinheiten)
    burst: float       # gesamte benötigte CPU-Zeit (Burst length)
    remaining: float   # verbleibende CPU-Zeit; wird durch __post_init__ initialisiert
    priority: int      # optional (für spätere Wochen)
```

**Wichtig:** `remaining` wird beim Start typischerweise auf `burst` gesetzt (siehe `__post_init__`). Die Simulation reduziert `remaining` während der Ausführung; Scheduler und Harness arbeiten mit denselben `Process`‑Objekten (Identität/Instanz muss beibehalten werden).

---

## 4. Scheduler‑API (erwartetes Verhalten)

Jede Scheduler‑Klasse (Referenz und Student) muss die Methode

```py
def schedule(self, processes: List[Process]) -> Optional[Process]:
    ...
```

bereitstellen.

**Kontrakt:**

* `processes` ist die **Ready‑Liste** (Liste von `Process`‑Objekten), die aktuell zur Auswahl steht.
* `schedule` gibt **entweder** eine `Process`‑Instanz (die **genau** in `processes` enthalten ist) zurück **oder** `None`, falls kein Prozess gewählt wurde.
* **FIFO Semantik (Referenz):** gibt das erste Element der Liste zurück. Es wird erwartet, dass die Simulation anschließend dieses Objekt aus `ready` entfernt und ausführt.

**Hinweis an Studierende:** geben Sie Ihr Scheduler‑Objekt niemals eine neue `Process`‑Instanz zurück — es muss die bestehende Instanz aus `ready` zurückgeben (Vergleich per Objekt‑Identität, nicht nur `pid`).

---

## 5. `run_simulation(scheduler, processes)` — Semantik & Ablauf

**Ziel:** Führe eine diskrete, einfache Simulation, die Scheduler‑Entscheidungen für CPU‑Zeit auswertet und für jeden Prozess `waiting` und `turnaround` berechnet.

**Ablauf (Kurz):**

1. `processes` wird nach `arrival` sortiert.
2. `time` beginnt bei `0.0`; `ready` ist leer; `completed` leer.
3. Solange noch `procs` (nicht‑angekommene Prozesse) **oder** `ready` vorhanden sind:

   * Verschiebe alle Prozesse mit `arrival <= time` von `procs` nach `ready`.
   * Falls `ready` leer: setze `time = procs[0].arrival` (nächste Ankunft) und fahre fort.
   * Rufe `p = scheduler.schedule(ready)` auf.

     * Falls `p is None`: setze `time = procs[0].arrival` (Scheduler hat niemanden gewählt).
     * Sonst: entferne `p` aus `ready`, führe `p` gemäss Policy aus (für FIFO: `time += p.remaining; p.remaining = 0`).
     * Berechne `start`, `finish`, `waiting = start - p.arrival`, `turnaround = finish - p.arrival` und füge `(pid, waiting, turnaround)` zu `completed`.
4. Gebe `completed` (Liste von Tupeln) zurück.

**Annahmen & Grenzen:**

* Dieses Modell ist **sequentiell** und vereinfacht: keine Kontext‑Switch‑Kosten, keine Nebenläufigkeit beim Ausführen eines Prozesses.
* FIFO ist **non‑preemptive** hier (vollständige Ausführung eines gewählten Prozesses). Bei preemptive Schedulers (RR, SRT) muss die Harness erweitert werden, damit `time` in Quanten voranschreitet und `remaining` nur teilweise reduziert wird.
* `run_simulation` verändert die `Process`‑Objekte (insb. `remaining`), daher sollte für mehrere Läufe eine **frische Kopie** der `Process`‑Liste verwendet werden.

---

## 6. Rückgabeformat und Interpretation

Die Rückgabe `completed` ist eine Liste von `(pid, waiting, turnaround)`‑Tupeln in der Reihenfolge der Fertigstellung. Beispiel:

```
[(1, 0.0, 100.0), (2, 100.1, 101.1), (3, 101.1, 102.1)]
```

* `waiting` = Wartezeit bis zur ersten Ausführung (Start - Arrival).
* `turnaround` = Fertigstellungszeit - Arrival.

Aus diesen Werten lassen sich einfache Aggregatmetriken berechnen:

* `avg_wait = sum(waiting) / n`
* `avg_turn = sum(turnaround) / n`

---

## 7. Tests — Aufbau & Zweck

**Wichtig:** Tests sind sowohl Lehrmittel als auch Selbstcheck. Die vorhandenen Tests decken zwei Bereiche ab:

1. **API/Unit‑Tests (Student API)** — `tests/test_student_scheduler.py`

   * Prüft, dass `StudentFifoScheduler` existiert und die erwartete Signatur hat.
   * Prüft Basisverhalten: leere Liste -> `None`, nicht‑leere -> erstes Element.

2. **Szenario/Metric‑Tests** — `tests/test_scheduler_metrics.py`

   * Führen konkrete Workloads (z. B. Convoy) auf der Referenz‑FIFO aus und prüfen robuste Eigenschaften (z. B. kurze Jobs warten deutlich länger).
   * Diese Tests sind **nicht** auf exakte Zeiten fixiert (um floating point / minimale scheduling Unterschiede robust zu tolerieren); stattdessen nutzen sie Ungleichheitschecks (z. B. `> 0.5`).

---

## 8. Testausführung & nützliche pytest‑Flags

Empfohlener Quickstart:

```bash
# ausführlichere Ausgabe (empfohlen für Studierende)
pytest -v -r a --tb=short

# oder nur die relevanten Tests
pytest tests/test_student_scheduler.py tests/test_scheduler_metrics.py -q
```

Erklärung häufiger Flags:

* `-v` verbose (listet jede Testfunktion)
* `-r a` show all extra summary info (skips/xfails)
* `--tb=short` kurze Tracebacks

Für CI / JUnit‑Reports:

```bash
pytest -v --junitxml=report.xml
```

---

## 9. Tipps zum Debugging typischer Fehler

* **`ImportError` (reference/student not found):** Stellen Sie sicher, dass Sie im Projekt‑Root arbeiten und `pip install -e .` ausgeführt haben — oder in Notebooks temporär `sys.path.append(os.path.abspath('.'))`.
* **`AssertionError` aus Tests:** Lies Traceback: pytest zeigt Datei und Ausdruck. Nutzen Sie `-v --tb=short` für kompakte Ausgabe.
* **`ValueError` beim `ready.remove(p)` in der Harness:** Bedeutet, der Scheduler hat ein Objekt zurückgegeben, das nicht in `ready` ist — häufige Ursachen:

  * Scheduler erzeugt neue `Process`‑Objekte anstatt vorhandene Instanzen zurückzugeben.
  * Erwartung: immer genau die Instanz aus `ready` zurückgeben.
* **Ergebnisse unterscheiden sich zwischen Notebook und Tests:** Prüfen Sie, ob die `Process`‑Instanzen mehrfach wiederverwendet wurden (z. B. `remaining` bereits 0) — für wiederholte Läufe benutzen Sie frische Instanzen oder setzen Sie `p.remaining = p.burst` zurück.

---

## 10. Wie man eigene Szenarien / Tests schreibt

**Beispiel einer neuen Testfunktion (nennen Sie sie `tests/test_my_scenario.py`):**

```py
from reference.scheduler import FifoScheduler, Process
from sim.simulator import run_simulation

def test_small_scenario():
    p1 = Process(pid=1, arrival=0.0, burst=2.0)
    p2 = Process(pid=2, arrival=0.5, burst=3.0)
    res = run_simulation(FifoScheduler(), [p1,p2])
    assert len(res) == 2
    waits = {pid: w for (pid,w,t) in res}
    assert waits[1] == 0.0
```

**Hinweis:** Verwenden Sie robuste Assertions (Ungleichheiten) wenn Floating Point / geringe Laufzeitdifferenzen möglich sind.
