import pytest
from week04.student.pcb import ProcessControlBlock, ProcessState


def test_pcb_lifecycle():
    pcb = ProcessControlBlock(pid=1, arrival=0.0, burst=5.0)
    assert pcb.state == ProcessState.NEW

    pcb.set_state(ProcessState.READY)
    assert pcb.state == ProcessState.READY

    pcb.set_state(ProcessState.RUNNING)
    assert pcb.state == ProcessState.RUNNING

    pcb.set_state(ProcessState.BLOCKED)
    assert pcb.state == ProcessState.BLOCKED

    pcb.set_state(ProcessState.READY)
    pcb.set_state(ProcessState.RUNNING)

    pcb.remaining = 0.0
    pcb.set_state(ProcessState.TERMINATED)
    assert pcb.is_terminated()


def test_snapshot_contains_fields():
    pcb = ProcessControlBlock(pid=2, arrival=1.0, burst=3.0)
    s = pcb.snapshot()
    assert s["pid"] == 2
    assert s["remaining"] == pcb.remaining
