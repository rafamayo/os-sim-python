import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

from common.process import Process
from week02.reference.scheduler import FifoScheduler, RoundRobinScheduler
from week02.sim.simulator import run_simulation_fifo, run_simulation_rr

def test_rr_improves_avg_wait_on_convoy():
    p1 = Process(pid=1, arrival=0.0, burst=100.0)
    p2 = Process(pid=2, arrival=0.1, burst=1.0)
    p3 = Process(pid=3, arrival=0.2, burst=1.0)
    procs = [p1, p2, p3]
    fifo = FifoScheduler()
    rr = RoundRobinScheduler(quantum=1.0)
    res_fifo = run_simulation_fifo(fifo, procs)
    res_rr = run_simulation_rr(rr, procs)
    avg_wait_fifo = sum(w for (_,w,_) in res_fifo)/len(res_fifo)
    avg_wait_rr = sum(w for (_,w,_) in res_rr)/len(res_rr)
    assert avg_wait_rr < avg_wait_fifo, 'RoundRobin should improve average waiting time in convoy scenario'
