from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Backend is running 🚀"})

@app.route('/api')
def api():
    return jsonify({
        "status": "success",
        "project": "multi-tier app",
        "data": "Hello from backend EC2"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)