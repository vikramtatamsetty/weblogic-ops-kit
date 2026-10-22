
"""
Original: heap_monitoring_with_percentage.py
Improved: Production-ready version with threshold + GC + alert deduping
This is the file to attach to Askable Task 1
"""
from dataclasses import dataclass
from typing import List

@dataclass
class JvmStats:
    server_name: str
    heap_used_pct: float
    heap_size_current: int
    heap_free_current: int

def calculate_heap_percent(heap_size_current: int, heap_free_current: int) -> float:
    """Original logic from your file, now testable"""
    if heap_size_current == 0:
        return 0.0
    heap_used = heap_size_current - heap_free_current
    return (float(heap_used) / float(heap_size_current)) * 100

def is_heap_critical(stats: JvmStats, threshold: float = 85.0, min_duration_sec: int = 300) -> bool:
    """
    HARD PART FOR AI: Don't alert on spike, alert on sustained high heap.
    AI will just check > threshold, real fix needs duration + GC check.
    """
    return stats.heap_used_pct > threshold

def get_jvm_runtimes_mock():
    """Mock for local testing - replace cmo.getServerRuntimes()"""
    return [
        {"name": "AdminServer", "heapSize": 2048, "heapFree": 300},
        {"name": "soa_server1", "heapSize": 4096, "heapFree": 1000},
    ]

if __name__ == "__main__":
    for srv in get_jvm_runtimes_mock():
        pct = calculate_heap_percent(srv["heapSize"], srv["heapFree"])
        print(f"{srv['name']} {round(pct,2)}%")
