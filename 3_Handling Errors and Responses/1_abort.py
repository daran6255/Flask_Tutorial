from flask import Flask, jsonify, request, abort

app = Flask(__name__)

items = {
    1: {"name": "Apple", "price": 10},
    2: {"name": "Banana", "price": 5}
}

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id not in items:
        abort(404, description="Item not found")
    return jsonify(items[item_id])

if __name__ == '__main__':
    app.run(debug=True)