from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Store latest ESP32 data
latest_data = {"voltage": 0.0, "current": 0.0}

@app.route('/esp32/data', methods=['POST'])
def receive_data():
    global latest_data
    body = request.get_json()
    latest_data = {
        "voltage": body.get("voltage", 0.0),
        "current": body.get("current", 0.0)
    }
    return jsonify({"status": "success", "received": True})

@app.route('/api/data', methods=['GET'])
def send_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
