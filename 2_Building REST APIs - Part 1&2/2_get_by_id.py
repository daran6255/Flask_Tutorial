from flask import Flask, jsonify

app = Flask(__name__)

# Sample data stored in a dictionary
items = {
    1: {"name": "Apple", "price": 10},
    2: {"name": "Banana", "price": 5}
}

# Route to get item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = items.get(item_id)
    return jsonify({
            "status": 200,
            "message": "Item found",
            "data": item
        }), 200
    # if item:
    #     return jsonify({
    #         "status": 200,
    #         "message": "Item found",
    #         "data": item
    #     }), 200
    # else:
    #     return jsonify({
    #         "status": 404,
    #         "message": "Item not found"
    #     }), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
