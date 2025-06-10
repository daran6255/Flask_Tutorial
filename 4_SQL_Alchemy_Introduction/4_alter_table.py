# ⚠️ Only works before table is created or requires raw SQL after creation
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Assume table already exists
@app.route('/alter-user-table')
def alter_user_table():
    try:
        db.session.execute('ALTER TABLE "user" ADD COLUMN age INTEGER')
        db.session.commit()
        return "User table altered: column 'age' added!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
