from flask import Flask

# Create a simple Flask application
app = Flask(__name__)  # __name__ is the entry point of the program

# Flask App Routing
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Hello bois</h1>"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

if __name__ == "__main__":
    app.run(debug=True)
