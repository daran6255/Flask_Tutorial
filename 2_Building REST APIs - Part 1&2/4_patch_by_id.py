from flask import Flask, jsonify, request

app = Flask(__name__)

items = {
    1: {"name": "Apple", "price": 10},
    2: {"name": "Banana", "price": 5}
}

# PATCH - Update part of item
@app.route('/items/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"status": 404, "message": "Item not found"}), 404

    data = request.json
    items[item_id].update(data)
    return jsonify({"status": 200, "message": "Item updated", "data": items[item_id], "updated_data": items}), 200

if __name__ == '__main__':
    app.run(debug=True)
