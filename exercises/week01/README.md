# Übungsblatt — Woche 01: Scheduler Basics (Python)

**Kurs:** Betriebssysteme (OS‑Simulator)\
**Dauer (empfohlen):** 90 Minuten Übungssitzung (+ Vor- und Nachbereitung)\
**Ort im Repo:** `exercises/week01/README.md`

---

## Lernziele

- Verstehen, was ein Scheduler tut (Ready‑Queue, Auswahl des nächsten Prozesses).
- Eine einfache FIFO‑Scheduler‑Strategie implementieren und testen.
- Mit Notebooks interaktiv entwickeln (JupyterLab / Google Colab).

---

## Vorbereitung (vor der Übung)

1. Repository klonen: `git clone <REPO-URL>` und in den Projektordner wechseln.
2. Virtuelle Umgebung anlegen und aktivieren (siehe `docs/Projekt-Quickstart.md`).
3. Abhängigkeiten installieren: `pip install -r requirements.txt`.
4. Optional: JupyterLab in der venv installieren oder das Notebook in Google Colab öffnen.
5. Prüfen: `pytest -q` (sollte die Referenz‑Tests ohne Fehler laufen lassen).

---

## Aufgaben (Schritt für Schritt)

### Aufgabe A — Demo und Orientierung (10–15 min)

1. Öffne das Notebook: `notebooks/week01_scheduler_basics.ipynb` (lokal in JupyterLab oder in Colab).
2. Führe die Demo‑Zellen aus, die die Referenz‑FIFO (`src/reference/scheduler.py`) zeigen.
3. Lies die Hinweise im Notebook zur `src/student/scheduler.py`.

**Ziel:** Du sollst die Idee hinter `FifoScheduler` verstehen und sehen, wie Prozesse modelliert werden.

---

### Aufgabe B — Implementiere `StudentFifoScheduler` (30–40 min)

1. Öffne `src/student/scheduler.py`.
2. Implementiere die Klasse `StudentFifoScheduler` mit der Methode `schedule(self, processes)`.
   - Erwartete Semantik: gib das erste Element aus `processes` zurück, oder `None` bei leerer Liste.
3. Führe die Testzellen im Notebook aus oder starte lokal: `pytest tests/test_scheduler.py -q`.

**Hinweis:** Die Tests prüfen die Referenzimplementation und — falls vorhanden — auch eure Student‑Implementierung.

---

### Aufgabe C — Kleine Erweiterung & Visualisierung (freiwillig, 15–30 min)

- Erweitere deinen Scheduler, sodass er eine Priority‑Funktion beachtet (höhere Priorität zuerst).
- Visualisiere die Ready‑Queue (z. B. mit `matplotlib`) und führe ein paar Szenarien durch (Arrival‑Zeit simulieren).

---

## Akzeptanzkriterien / Selbsttest

- `pytest` läuft lokal durch (alle Tests grün).
- `src/student/scheduler.py` enthält `StudentFifoScheduler` und eine passende `Process`‑Dataclass.
- Notebook‑Zellen lassen sich ohne Fehler ausführen und zeigen die erwarteten Ausgaben.

---

## Hinweise zur Abgabe / Sichtbarkeit

- **Keine formale Abgabe:** Es gibt in dieser Woche keine verpflichtende Einreichung.
- **Backup (empfohlen):** Studierende können optional ihren aktuellen Branch in ein persönliches Remote‑Repo pushen (z. B. `git push origin wk01/<matrikelnummer>`), um ein Backup zu haben und bei Bedarf per Link vorzuzeigen.
- **Präsentation im Hörsaal:** In der Übung werden 3–4 Studierende ihre Lösung kurz (5–8 min) präsentieren. Bereite eine kurze Demo (Notebook + ggf. `pytest` Ergebnis) vor.

---

## Troubleshooting (Kurz)

- **ImportError:** Stelle sicher, dass das `src`‑Verzeichnis im Python‑Pfad ist (oder benutze `pip install -e .`).
- **überspringt Student‑Test:** Der Test überspringt die Student‑Prüfung, wenn `src.student.scheduler` nicht importierbar ist — kontrolliere Dateiname/Package.
- **PowerShell ExecutionPolicy:** Windows‑Nutzende folgen `docs/Projekt-Quickstart.md` für die Lösung.


