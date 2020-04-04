from flask import jsonify
from app import app


@app.route('/health')
def health_check():
    """
        Route to be used as health-check endpoint for the ECS target group.
    """
    return jsonify({"status": "OK"})
