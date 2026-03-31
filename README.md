**Traffic Analyzer API**

A Python service that:

- Logs incoming HTTP requests
  - Tracks:
    request count
- IPs
  endpoints hit
- Exposes:
  /metrics → Prometheus-style metrics
  /stats → JSON analytics
