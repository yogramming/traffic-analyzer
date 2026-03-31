from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

request_count = 0
endpoint_hits = defaultdict(int)
ip_hits = defaultdict(int)


@app.before_request
def track():
    global request_count
    request_count += 1
    endpoint_hits[request.path] += 1
    ip_hits[request.remote_addr] += 1


@app.route('/')
def home():
    return "Traffic Analyzer Running 🚀"


@app.route('/stats')
def stats():
    return jsonify({
        "total_requests": request_count,
        "endpoints": dict(endpoint_hits),
        "ips": dict(ip_hits)
    })


@app.route('/metrics')
def metrics():
    return f"""
# HELP requests_total Total requests
# TYPE requests_total counter
requests_total {request_count}
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
