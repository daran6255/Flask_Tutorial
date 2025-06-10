from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'test'  # Change to a strong key in production

jwt = JWTManager(app)

users = {
    "admin": "12345",
    "user": "abcd"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def protected():
    # Authorization: Bearer <your_token>
    current_user = get_jwt_identity()
    return jsonify(message=f"Welcome {current_user}, this is a protected route!")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
