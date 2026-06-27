from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os
import sqlite3

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Статическая метрика с инфо о приложении
metrics.info('app_info', 'Application info', version='1.0.2')

DB_PATH = os.getenv('DATABASE_URL', 'app_database.db')

def check_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.close()
        return True
    except sqlite3.Error:
        return False

@app.route('/')
def index():
    return jsonify({
        "status": "Running",
        "service": "Flask Metrics Exporter",
        "version": "1.0.2"
    })

@app.route('/health')
def health():
    db_ok = check_db()
    return jsonify({
        "status": "UP" if db_ok else "DEGRADED",
        "database": "Connected" if db_ok else "Disconnected"
    }), 200 if db_ok else 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
