from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for your Flask application
@app.route('/')
def index():
    output = ""
    for i in range(0, 3):
        output += "jai shri ram<br>"
    return output

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
