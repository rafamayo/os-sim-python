## Empfohlener, robusterer Ablauf mit Kommandos

### 1) Repo klonen

```bash
git clone <REPO-URL>
cd os-sim-python
```

### 2) virt. Umgebung erzeugen (im Projektordner)

> Verwende eine versteckte Ordner-Konvention wie `.venv` (gängig).

**Linux / macOS**

```bash
python3 -m venv .venv
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
```

### 3) venv aktivieren (wichtig — vor jedem Arbeitstag / neuem Terminal)

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (cmd.exe)**

```cmd
.\.venv\Scripts\activate.bat
```

> Nach Aktivierung sollte der Prompt `(.venv)` anzeigen. Wenn nicht, prüfe die Pfade.

### 4) pip updaten & Abhängigkeiten installieren

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

> Wenn du JupyterLab in der venv möchtest (empfohlen), füge `jupyterlab` zu `requirements.txt` oder installiere es extra:

```bash
pip install jupyterlab
```

### 5) (Optional, empfohlen) Kernel für Jupyter registrieren

Damit JupyterLab automatisch die venv nutzt, registriere den Kernel:

```bash
python -m ipykernel install --user --name=os-sim --display-name "OS-Sim (.venv)"
```

Dann in JupyterLab: Kernel → **OS-Sim (.venv)** auswählen.

### 6) JupyterLab starten

```bash
jupyter lab
```

oder wenn nur Notebook:

```bash
jupyter notebook
```

### 7) Entwickeln

* Notebook öffnen (`notebooks/week01_...ipynb`) und Zellen ausführen.
* Änderungen in `src/student/...` vornehmen.
* Tests lokal ausführen:

```bash
pytest -q
```

### 8) Deaktivieren der venv (am Ende)

```bash
deactivate
```

---

## Wichtige Hinweise / Tipps & Troubleshooting

* **Aktivierung ist nötig**: Jedes neue Terminal benötigt wieder `source .venv/bin/activate` (oder Windows-Äquivalent). Alternativ kannst du immer `./.venv/bin/python` (Linux/macOS) bzw. `.\.venv\Scripts\python.exe` (Windows) verwenden, um sicher die richtige Python-Executable zu nutzen.
* **`.venv` in `.gitignore`**: füge `.venv/` zur `.gitignore` hinzu, damit die virtuelle Umgebung nicht committed wird.
* **Wenn `Activate.ps1` scheitert (ExecutionPolicy)**: PowerShell-Fehler kannst du mit `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` beheben (Admin-Rechte evtl. nötig) — beschreibe das vorsichtig den Studierenden.
* **Wenn `ImportError: module not found` in Notebook**: Entweder `pip install -e .` (editable install) oder oben im Notebook `import sys, os; sys.path.append(os.path.abspath('src'))` verwenden.
* **JupyterLab in venv installieren**: sehr zu empfehlen — dann sind Kernel & Pakete sofort passend. Installiere Jupyter **in der venv**, nicht global.
* **Python-Version prüfen**: `python --version` → verwende die in den Kurs-Anforderungen genannte Version (z. B. 3.10+).
* **Wenn viele GUI/extension-Probleme**: nutze statt lokal Colab / Codespaces als Fallback.
* **Windows & WSL2**: Windows-Nutzer ohne Entwicklerrechte sollten WSL2 verwenden — meist die stabilste Option für Linux-like behavior.

---

## Minimaler „One-liner“ für erfahrene Nutzer (Linux/macOS)

```bash
git clone <URL> && cd repo && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt jupyterlab && python -m ipykernel install --user --name=os-sim --display-name "OS-Sim (.venv)" && jupyter lab
```

(Erklärend: das erstellt venv, aktiviert, installiert Abhängigkeiten + jupyterlab, registriert Kernel und startet JupyterLab.)

---

## Alternative / Fallbacks, falls Probleme auftreten

* **Google Colab**: kein Setup nötig; öffne Notebook über *File → Open notebook → GitHub*. Änderungen persistieren nur wenn du Dateien aktiv commitest (oder in Drive speicherst).
* **Devcontainer / Docker**: falls wiederkehrende lokale Probleme auftreten, biete Devcontainer als einheitliche Umgebung an.
* **VS Code Remote / Codespaces / Gitpod**: gute browser- oder cloudbasierte Alternativen.
