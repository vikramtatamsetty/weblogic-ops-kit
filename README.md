
# WebLogic Operations Automation Kit

Production-grade Python toolkit for Oracle WebLogic / Fusion Middleware monitoring.
Built from real incident automation used in enterprise environments.

## Modules (from your original files)

- `heap_monitor.py` - from heap_monitoring_with_percentage.py
- `thread_monitor.py` - from struckthreadcheckcount.py + threadpoolcheck.py
- `jdbc_monitor.py` - from JDBC_monitoring_all*.py
- `server_inventory.go` - from Check_all_servers.go + Config_details.go

## Why this is hard for AI

- WLST vs Python boundary
- PID/restart race conditions
- Stuck-thread false positives on SOA/OSB
- Log rotation + multi-line stack traces
- JDBC pool states: Active vs Failed vs Reconnect failures

## Run with Docker
```
docker build -t wls-ops .
docker run wls-ops
```

## Run tests
```
pip install -r requirements.txt
pytest
```
