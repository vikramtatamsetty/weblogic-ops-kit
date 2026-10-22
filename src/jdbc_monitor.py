
"""
Original: JDBC_monitoring_all.py + _active_check + _failed_check
Improved: Unified monitor with failure classification
"""
from dataclasses import dataclass

@dataclass
class JdbcStats:
    server: str
    datasource: str
    active_current: int
    failures_to_reconnect: int
    state: str

def is_datasource_unhealthy(stats: JdbcStats) -> bool:
    """
    AI FAILS: AI checks only active count
    Correct: Must check failures_to_reconnect + state + active spike
    """
    if stats.failures_to_reconnect > 0:
        return True
    if stats.state != "Running":
        return True
    # Active count alone is not failure - pool can be busy
    return False
