
from src.heap_monitor import calculate_heap_percent, JvmStats, is_heap_critical

def test_heap_percent_calculation():
    assert calculate_heap_percent(1000, 200) == 80.0
    assert calculate_heap_percent(2048, 0) == 100.0
    assert calculate_heap_percent(0, 0) == 0.0

def test_heap_critical_threshold():
    stats_ok = JvmStats("soa_server1", 70.0, 1000, 300)
    stats_crit = JvmStats("soa_server1", 90.0, 1000, 100)
    assert is_heap_critical(stats_ok) == False
    assert is_heap_critical(stats_crit) == True
