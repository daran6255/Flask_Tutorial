## CRUD Operations in Flask (with SQLAlchemy)

### CRUD stands for:
	Create → Add new data
	Read → Get data
	Update → Change existing data
	Delete → Remove data

We'll use a basic User model for these operations.

| Operation | Method | Route         | Description         |
| --------- | ------ | ------------- | ------------------- |
| Create    | POST   | `/users`      | Add a new user      |
| Read      | GET    | `/users`      | Get all users       |
| Read      | GET    | `/users/<id>` | Get one user        |
| Update    | PUT    | `/users/<id>` | Update user details |
| Delete    | DELETE | `/users/<id>` | Delete a user       |
