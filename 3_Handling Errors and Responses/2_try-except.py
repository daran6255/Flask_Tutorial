from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/divide', methods=['POST'])
def divide():
    try:
        data = request.get_json()
        x = int(data.get('x'))
        y = int(data.get('y'))
        result = x / y
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Custom error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found", "status": 404}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request", "status": 400}), 400

if __name__ == '__main__':
    app.run(debug=True)
