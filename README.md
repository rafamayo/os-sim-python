# OS-Simulator (Python) — Course Skeleton

Dieses Repository ist ein leichtgewichtiges Kurs-Skeleton für den OS-Simulator in **Python**.
Ziel: Konzepte interaktiv mit Notebooks demonstrieren und in `src/` kleine Module implementieren.

Struktur:
```
os-sim-python/
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ reference/
│  │  └─ scheduler.py
│  └─ student/
│     └─ scheduler.py
├─ notebooks/
│  └─ week01_scheduler_basics.ipynb
├─ tests/
│  └─ test_scheduler.py
├─ .github/
│  └─ workflows/ci.yml
└─ tools/
   └─ run_notebook_check.py
```

Quickstart (lokal):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Colab:
- Öffnen Sie `notebooks/week01_scheduler_basics.ipynb` via *File → Open notebook → GitHub* in Google Colab.
- Die Notebook-Zellen verwenden die Referenz-Implementierung für Demo; implementieren Sie Ihre eigene Version unter `src/student/scheduler.py`.

CI:
- GitHub Actions (Ubuntu) führt `pytest` aus.

Viel Spaß beim Ausprobieren — die Week-01-Notebooks sind als Einstieg gedacht.
