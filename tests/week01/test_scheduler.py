import importlib
import pytest

# Test reference scheduler
from week01.reference.scheduler import FifoScheduler, Process as RefProcess

def test_reference_fifo_empty():
    s = FifoScheduler()
    assert s.schedule([]) is None

def test_reference_fifo_order():
    s = FifoScheduler()
    p1 = RefProcess(pid=1)
    p2 = RefProcess(pid=2)
    assert s.schedule([p1, p2]).pid == 1

#def test_student_scheduler_if_exists():
def test_student_scheduler_exists():
    mod = importlib.import_module("week01.student.scheduler")
    cls = getattr(mod, "StudentFifoScheduler", None)
    assert cls is not None, "Definiert eine Klasse StudentFifoScheduler in src/student/scheduler.py"

def test_student_fifo_behaviour():
    mod = importlib.import_module("week01.student.scheduler")
    P = getattr(mod, "Process", None)
    S = getattr(mod, "StudentFifoScheduler", None)
    assert P is not None and S is not None

    s = S()
    p1 = P(pid=1)
    p2 = P(pid=2)
    chosen = s.schedule([p1, p2])
    assert chosen is p1, "FIFO: erster Prozess in der ready-list muss gewählt werden"
    assert s.schedule([]) is None, "Leere ready-list -> None"
