from flask import Flask, jsonify, request

app = Flask(__name__)

items = {
    1: {"name": "Apple", "price": 10},
    2: {"name": "Banana", "price": 5},
    3: {"name": "Orange", "price": 8},
    4: {"name": "Mango", "price": 15},
    5: {"name": "Grapes", "price": 12},
}

# DELETE - Remove item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"status": 404, "message": "Item not found"}), 404

    deleted_item = items.pop(item_id)
    return jsonify({
        "status": 200,
        "message": f"Item {item_id} deleted successfully",
        "deleted_item": deleted_item,
        "updated_items": items
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
