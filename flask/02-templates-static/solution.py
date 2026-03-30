from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key"

# In-memory store
items = []
next_id = 1


# Exercise 2: Item List Page
@app.route("/items")
def list_items():
    pass


# Exercise 3: Item Form
@app.route("/items/new")
def new_item_form():
    pass


@app.route("/items", methods=["POST"])
def create_item():
    pass


# Exercise 4: Detail Page with Macro
@app.route("/items/<int:item_id>")
def item_detail(item_id):
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5000)
