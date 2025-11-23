from common.process import Process
from week01.reference.scheduler import FifoScheduler
from week01.sim.simulator import run_simulation


def test_fifo_convoy():
    # Convoy scenario: one long job arrives first, then two short jobs
    p1 = Process(pid=1, arrival=0.0, burst=100.0)
    p2 = Process(pid=2, arrival=0.1, burst=1.0)
    p3 = Process(pid=3, arrival=0.2, burst=1.0)
    res = run_simulation(FifoScheduler(), [p1, p2, p3])
    # Convert to dict pid -> waiting
    waits = {pid: w for (pid, w, t) in res}
    # p1 should start immediately
    assert waits[1] == 0.0
    # p2 and p3 must wait a long time (greater than a small threshold)
    assert waits[2] > 0.5
    assert waits[3] > 0.5
