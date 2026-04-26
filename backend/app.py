from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # 👈 IMPORTANT FIX

@app.route('/')
def home():
    return jsonify({"message": "Backend running"})

@app.route('/api')
def api():
    return jsonify({
        "status": "success",
        "data": "Hello from EC2 backend"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)