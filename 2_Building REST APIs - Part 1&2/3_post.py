from flask import Flask, request, jsonify

app = Flask(__name__)

# List to store items
items = []

# Route to add a new item
@app.route('/items/create', methods=['POST'])
def add_item():
    # Get the data sent in the request
    data = request.get_json()

    # Add the item to the list
    items.append(data)

    # Return a success message with the added item
    return jsonify({
        "status": 201,
        "message": "Item added successfully",
        "data": items
    }), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
