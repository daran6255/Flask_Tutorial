from flask import Flask, jsonify

app = Flask(__name__)

items = {
    1: {"name": "Apple", "price": 10},
    2: {"name": "Banana", "price": 5}
}

@app.route('/items', methods=['GET'])
def get_items():
    # return items
    return jsonify({
        "status": 200,
        "message": "Items fetched successfully",
        "data": items
    }), 200
    
if __name__ == '__main__':
    app.run(debug=True)
