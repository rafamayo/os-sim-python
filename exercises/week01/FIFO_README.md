This folder contains the additional files for Week 1 FIFO demonstration.

Place the files under the following paths in your course repo (if not already present):

- src/reference/scheduler.py  (reference FIFO + Process with arrival/burst)
- src/student/scheduler.py    (student starter)
- src/sim/simulator.py        (simulation harness run_simulation)
- tests/test_scheduler_metrics.py (convoy test)

Run locally:
- create and activate venv
- pip install -e .
- pytest -q

Or open notebooks/week01_scheduler_basics.ipynb and execute the Convoy experiment cells.
