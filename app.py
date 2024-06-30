from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and a corresponding view function
@app.route('/')
def index():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
