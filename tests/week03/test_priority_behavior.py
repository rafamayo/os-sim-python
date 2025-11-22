import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

from common.process import Process
from week03.reference.scheduler import PriorityScheduler, SrtScheduler, SjfScheduler
from week03.sim.simulator import run_simulation_priority, run_simulation_srt, run_simulation_sjf

def test_priority_selects_highest():
    p1 = Process(pid=1, arrival=0.0, burst=5.0, priority=10)
    p2 = Process(pid=2, arrival=0.0, burst=5.0, priority=0)
    sched = PriorityScheduler()
    chosen = sched.schedule([p1,p2])
    assert chosen.pid == 2, 'PriorityScheduler should pick lower numeric priority value (higher priority)'

def test_srt_improves_over_sjf_on_example():
    p1 = Process(pid=1, arrival=0.0, burst=8.0)
    p2 = Process(pid=2, arrival=1.0, burst=4.0)
    p3 = Process(pid=3, arrival=2.0, burst=1.0)
    procs = [p1,p2,p3]
    sjf = SjfScheduler()
    srt = SrtScheduler()
    res_sjf = run_simulation_sjf(sjf, procs)
    res_srt = run_simulation_srt(srt, procs)
    avg_wait_sjf = sum(w for (_,w,_) in res_sjf)/len(res_sjf)
    avg_wait_srt = sum(w for (_,w,_) in res_srt)/len(res_srt)
    assert avg_wait_srt <= avg_wait_sjf, 'SRT should have equal or lower average waiting time in this scenario'
