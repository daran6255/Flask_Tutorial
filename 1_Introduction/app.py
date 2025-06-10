# Importing the Flask class from the flask package
from flask import Flask

# Creating a Flask app instance
# __name__ is a special variable in Python that holds the name of the current module
# Flask uses this to know where to look for resources like templates and static files
app = Flask(__name__)

# Defining a route for the home page ('/')
# This decorator tells Flask to run the `hello()` function when someone accesses the root URL
@app.route('/')
def hello():
    # This function returns a simple text response to the browser
    return "Hello, World hi"

# This block ensures the app runs only if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Runs the Flask development server with debug mode ON
    # debug=True helps in automatic code reload and shows helpful error messages
    app.run(debug=True)
