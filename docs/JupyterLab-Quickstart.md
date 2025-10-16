# JupyterLab – Quickstart (Windows / macOS / Linux)

Kurzanleitung: In 6 Schritten JupyterLab starten, Projekt-Dependencies installieren und das Week-01-Notebook ausführen.

> **Voraussetzungen:** Python 3.8+ installiert. Git installiert (oder GitHub-Web-UI nutzen).
> Wenn du keinen Python-Install willst: nutze stattdessen **Google Colab** (öffne das Notebook über *File → Open notebook → GitHub*).

---

## 1. Repository klonen

```bash
git clone <REPO-URL>
cd os-sim-python
```

---

## 2. Virtuelle Umgebung anlegen (empfohlen)

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

> Nach Aktivierung sollte dein Prompt `(.venv)` enthalten.

Prüfe Versionen:

```bash
python --version
pip --version
```

---

## 3. Abhängigkeiten installieren

```bash
pip install --upgrade pip
pip install -r requirements.txt
# Optional: für bessere Notebook-Entwicklung
pip install jupyterlab jupyterlab-git
```

Falls du die Module importierbar machen willst:

```bash
pip install -e .
```

(Ermöglicht `from simulator import ...` falls `setup.py`/`pyproject` vorhanden ist.)

---

## 4. JupyterLab starten

```bash
jupyter lab
```

* Browser öffnet JupyterLab; wähle das Projektverzeichnis.
* Wähle oben rechts im Notebook-Menü den Kernel `Python` (oder `OS-Sim (venv)`, falls angelegt).

---

## 5. Notebook öffnen & ausführen

* Öffne `notebooks/week01_scheduler_basics.ipynb`.
* Führe Zellen nacheinander aus (Shift + Enter).
* Wenn du Änderungen in `src/student/...` machst: Zellen neu ausführen, um Effekte zu sehen.

---

## 6. Tests lokal ausführen (Schnellkontrolle)

```bash
pytest -q
# oder nur Week01-Test:
pytest tests/test_scheduler.py -q
```

Grün = alles gut. Bei Fehlern: prüfe Konsolen-/Traceback-Ausgabe.

---

## Kurze Troubleshooting-Tips

* **ImportError (Module not found):** Entweder `pip install -e .` ausführen oder zu Beginn des Notebooks `import sys, os; sys.path.append(os.path.abspath('src'))`.
* **Kernel startet nicht / stürzt ab:** große Zellen aufteilen; venv korrekt aktiviert? `which python` prüfen.
* **Notebook-Änderungen nicht sichtbar:** nach Edit speichern (Ctrl+S) & Kernel neu starten (Kernel → Restart & Run All).
* **Windows PowerShell-Ausführungsfehler beim Aktivieren:** nutze `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` oder verwende CMD: `.\.venv\Scripts\activate.bat`.
* **Wenn lokal zu schwierig:** öffne Notebook in **Google Colab** (File → Open notebook → GitHub → Repo → Notebook).

---

## Hilfe & Support

* Poste ein Issue im Kurs-Repo mit:

  * `python --version`, `pip freeze` (oder `requirements.txt`), Fehler-Log (pytest output).
* Office Hour / Forum: bring dein Notebook geöffnet mit Bildschirmfreigabe mit.

---

Viel Erfolg — starte mit `notebooks/week01_scheduler_basics.ipynb`. Wenn du willst, erstelle ich zusätzlich ein kurzes Setup-Skript (`setup_env.sh` / `setup_env.ps1`) zum automatischen Einrichten.
