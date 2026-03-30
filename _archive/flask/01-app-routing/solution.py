from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# In-memory store for exercise 3
items = []
next_id = 1


# Exercise 1: Hello App
@app.route("/")
def hello():
    pass


# Exercise 2: Route Parameters
@app.route("/greet/<name>")
def greet(name):
    pass


@app.route("/square/<int:number>")
def square(number):
    pass


# Exercise 3: JSON API Routes
@app.route("/api/items", methods=["GET"])
def get_items():
    pass


@app.route("/api/items", methods=["POST"])
def create_item():
    pass


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    pass


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    pass


# Exercise 4: Request Inspection
@app.route("/debug", methods=["GET", "POST", "PUT", "DELETE"])
def debug():
    pass


# Exercise 5: Error Handlers
@app.errorhandler(404)
def not_found(e):
    pass


@app.errorhandler(500)
def server_error(e):
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5000)
