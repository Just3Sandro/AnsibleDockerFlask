from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL")

@app.route('/')
def home():
    return jsonify({"message": "Flask App is Running!"})

@app.route('/ping')
def ping():
    return jsonify({"ping": "pong"})

@app.route('/db-status')
def db_status():
    try:
        conn = psycopg2.connect(DB_URL)
        conn.close()
        return jsonify({"database": "connected"})
    except:
        return jsonify({"database": "not connected"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

