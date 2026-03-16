from flask import Flask, jsonify

app = Flask(__name__)

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Hello from Docker Flask API!"

# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # Run on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)