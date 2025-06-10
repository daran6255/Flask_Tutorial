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
