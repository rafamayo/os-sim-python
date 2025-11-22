import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

def test_student_stubs_exist():
    mod = __import__('week03.student.scheduler', fromlist=['*'])
    assert hasattr(mod, 'StudentPriorityScheduler'), 'StudentPriorityScheduler missing'
    assert hasattr(mod, 'StudentSrtScheduler'), 'StudentSrtScheduler missing'
    S = mod.StudentPriorityScheduler()
    T = mod.StudentSrtScheduler()
    try:
        S.schedule([])
    except NotImplementedError:
        pass
    try:
        T.schedule([])
    except NotImplementedError:
        pass
