from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:12345@localhost:5432/test"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# post or create new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "User created",
                "user": {
                    "id": new_user.id,
                    "name": new_user.name,
                    "email": new_user.email,
                },
            }
        ),
        201,
    )

@app.route('/users/multiple', methods=['POST'])
def create_multiple_users():
    data = request.json  # expecting a list of user dicts
    created_users = []

    for user_data in data:
        new_user = User(name=user_data['name'], email=user_data['email'])
        db.session.add(new_user)
        created_users.append({"name": new_user.name, "email": new_user.email})

    db.session.commit()
    return jsonify({"message": f"{len(created_users)} users created", "users": created_users}), 201


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
