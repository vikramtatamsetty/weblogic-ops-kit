
"""
Original: struckthreadcheckcount.py + threadpoolcheck.py
Improved: This is your BEST Askable task - stuck thread false positive handling

Attach THIS file as your Askable task example
"""
from dataclasses import dataclass
from typing import List, Set

# Known long-running SOA/OSB patterns that are NOT stuck
SOA_LONG_RUNNING_PATTERNS = {
    "oracle.soa", "com.bea.wli", "bpel", "osb", "mediator"
}

@dataclass
class ThreadInfo:
    name: str
    state: str
    stack_trace: str
    stuck_duration_sec: int

def is_true_stuck_thread(thread: ThreadInfo, long_running_allowlist: Set[str] = None) -> bool:
    """
    ORIGINAL CODE: tp.getStuckThreadCount() - just prints count
    IMPROVED: Distinguish true stuck vs SOA/OSB long-running

    AI FAILS HERE: AI will flag any thread with STUCK in name
    Correct: Check duration + stack pattern + allowlist
    """
    if long_running_allowlist is None:
        long_running_allowlist = SOA_LONG_RUNNING_PATTERNS

    # SOA/BPEL threads can run 10+ mins legitimately
    if any(p in thread.stack_trace.lower() for p in long_running_allowlist):
        return thread.stuck_duration_sec > 1800  # 30 min for SOA

    return thread.stuck_duration_sec > 600  # 10 min for normal

def detect_stuck_threads(threads: List[ThreadInfo]) -> List[ThreadInfo]:
    return [t for t in threads if is_true_stuck_thread(t)]

# Mock for grading
def get_mock_threads():
    return [
        ThreadInfo("ExecuteThread: '5' for queue: 'weblogic.kernel.Default'", "STUCK", "java.net.SocketInputStream.socketRead", 900),
        ThreadInfo("BPEL Invoke", "STUCK", "oracle.soa.bpel.engine.dispatch", 800),  # should NOT be flagged
        ThreadInfo("OSB Pipeline", "STUCK", "com.bea.wli.sb.pipeline", 2000),  # should be flagged after 30m
    ]
