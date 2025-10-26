from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to CI/CD Demo!",
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({
        "operation": "addition",
        "result": a + b
    })

# Alternative route for negative numbers using query params
@app.route('/add')
def add_query():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        return jsonify({
            "operation": "addition",
            "result": a + b
        })
    return jsonify({"error": "Missing parameters"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)