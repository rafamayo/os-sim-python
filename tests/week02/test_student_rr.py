import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

def test_student_module_exists_and_smoke():
    try:
        mod = __import__('week02.student.scheduler', fromlist=['*'])
    except Exception as e:
        raise AssertionError(f"Could not import student.scheduler: {e}")
    S = getattr(mod, 'StudentRoundRobinScheduler', None)
    P = getattr(__import__('common.process', fromlist=['*']), 'Process')
    assert S is not None and P is not None, 'Student module must define StudentRoundRobinScheduler and Process'
    s = S(quantum=1.0)
    p1 = P(pid=1)
    # should not raise NotImplementedError
    try:
        s.schedule([p1])
    except NotImplementedError:
        raise AssertionError('StudentRoundRobinScheduler.schedule still raises NotImplementedError')
