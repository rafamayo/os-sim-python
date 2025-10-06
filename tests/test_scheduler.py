import importlib
import pytest

# Test reference scheduler
from src.reference.scheduler import FifoScheduler, Process as RefProcess

def test_reference_fifo_empty():
    s = FifoScheduler()
    assert s.schedule([]) is None

def test_reference_fifo_order():
    s = FifoScheduler()
    p1 = RefProcess(pid=1)
    p2 = RefProcess(pid=2)
    assert s.schedule([p1, p2]).pid == 1

# If student implementation exists, run the same tests against it (optional)
def test_student_scheduler_if_exists():
    try:
        student_mod = importlib.import_module('src.student.scheduler')
    except Exception:
        pytest.skip('Student scheduler not present')
    # expect class StudentFifoScheduler
    cls = getattr(student_mod, 'StudentFifoScheduler', None)
    assert cls is not None, "Student module must define StudentFifoScheduler"
    s = cls()
    P = getattr(student_mod, 'Process', None)
    assert P is not None, "Student module must define Process dataclass"
    assert s.schedule([]) is None
    p1 = P(pid=11)
    p2 = P(pid=12)
    assert s.schedule([p1, p2]).pid == 11
