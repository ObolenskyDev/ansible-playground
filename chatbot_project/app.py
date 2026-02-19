from flask import Flask, jsonify
import os
import sqlite3 # Используем для простоты демо, или Postgres если хочешь усложнить

app = Flask(__name__)

# Имитация работы с БД
DB_PATH = os.getenv('DATABASE_URL', 'app_database.db')

def check_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.close()
        return True
    except:
        return False

@app.route('/')
def index():
    return jsonify({
        "status": "Running",
        "service": "Enterprise Gateway",
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
    # Слушаем на всех интерфейсах для Docker
    app.run(host='0.0.0.0', port=5000)