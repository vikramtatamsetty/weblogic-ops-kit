
from src.thread_monitor import ThreadInfo, is_true_stuck_thread, detect_stuck_threads

def test_soa_long_running_not_flagged_as_stuck():
    """SOA thread running 13 mins - should NOT be flagged (common AI failure)"""
    t = ThreadInfo("BPEL", "STUCK", "oracle.soa.bpel.engine.dispatch", 800)
    assert is_true_stuck_thread(t) == False

def test_true_stuck_thread_flagged():
    """Normal thread stuck 15 mins - SHOULD be flagged"""
    t = ThreadInfo("ExecuteThread", "STUCK", "java.net.SocketInputStream.socketRead", 900)
    assert is_true_stuck_thread(t) == True

def test_osb_long_running_threshold():
    """OSB thread at 20 mins - not yet, at 35 mins - yes"""
    t_short = ThreadInfo("OSB", "STUCK", "com.bea.wli.sb.pipeline", 1200)
    t_long = ThreadInfo("OSB", "STUCK", "com.bea.wli.sb.pipeline", 2000)
    assert is_true_stuck_thread(t_short) == False
    assert is_true_stuck_thread(t_long) == True

def test_lazy_ai_solution_fails():
    """Lazy AI would just check 'STUCK' in name - should fail our tests"""
    # If someone does `return 'STUCK' in thread.state`, this will catch it
    threads = [
        ThreadInfo("BPEL", "STUCK", "oracle.soa.bpel", 100),
        ThreadInfo("Normal", "RUNNING", "some code", 0),
    ]
    result = detect_stuck_threads(threads)
    assert len(result) == 0  # Neither should be flagged
