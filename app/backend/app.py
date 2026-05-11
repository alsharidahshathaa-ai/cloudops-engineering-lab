from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint was accessed")
    return jsonify({
        "message": "CloudOps Lab Running"
    })

@app.route("/health")
def health():
    app.logger.info("Health check endpoint was accessed")
    return jsonify({
        "status": "healthy"
    })

@app.route("/env")
def env():
    current_env = os.getenv("ENV", "not set")
    app.logger.info(f"Environment endpoint was accessed. ENV={current_env}")
    return jsonify({
        "environment": current_env
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
