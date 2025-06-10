from flask import Flask, jsonify, request

app = Flask(__name__)

items = {
    1: {"name": "Apple", "price": 10},
    2: {"name": "Banana", "price": 5}
}

# PUT - Replace item entirely
@app.route('/items/<int:item_id>', methods=['PUT'])
def replace_item(item_id):
    if item_id not in items:
        return jsonify({"status": 404, "message": "Item not found"}), 404

    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"status": 400, "message": "Invalid data"}), 400

    items[item_id] = {"name": data["name"], "price": data["price"]}
    return jsonify({"status": 200, "message": "Item replaced", "data": items[item_id], "updated_data": items}), 200

if __name__ == '__main__':
    app.run(debug=True)
