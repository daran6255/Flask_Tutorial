## What is SQLAlchemy?
SQLAlchemy is a powerful Python library used to interact with databases. It works like a "bridge" between Python code and SQL databases.

### Features:
1. Lets you write Python code instead of SQL queries.
2. Supports many databases like PostgreSQL, MySQL, SQLite.
3. Has ORM (Object Relational Mapping): You can treat database tables like Python classes.
---
### Setting Up PostgreSQL with Flask
	pip install flask flask_sqlalchemy psycopg2-binary
	
### Basic Setup to Connect with PostgreSQL

	from flask import Flask
	from flask_sqlalchemy import SQLAlchemy

	app = Flask(__name__)

	# PostgreSQL connection URI
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/test'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db = SQLAlchemy(app)

	# Simple route to test database connection
	@app.route('/')
	def check_db():
		try:
			# Test a raw SQL query
			db.session.execute('SELECT 1')
			return "Database connected successfully!"
		except Exception as e:
			return f"Database connection failed: {e}"

	if __name__ == '__main__':
		app.run(debug=True)

### Creating Models Using SQLAlchemy ORM
A Model represents a database table, and each attribute is a column.

	class User(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(100), nullable=False)
		email = db.Column(db.String(120), unique=True, nullable=False)

### Creating the Table in the Database
You can create all tables defined using:
with app.app_context():
    db.create_all()

example: 
	@app.route('/create-tables')
	def create_tables():
		db.create_all()
		return "Tables created!"
