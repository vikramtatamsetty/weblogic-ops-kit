
from src.jdbc_monitor import JdbcStats, is_datasource_unhealthy

def test_jdbc_failure_detected():
    stats = JdbcStats("soa_server1", "SOADataSource", 5, 3, "Running")
    assert is_datasource_unhealthy(stats) == True

def test_jdbc_busy_but_healthy():
    """High active count alone is NOT unhealthy - AI often fails here"""
    stats = JdbcStats("soa_server1", "SOADataSource", 50, 0, "Running")
    assert is_datasource_unhealthy(stats) == False
