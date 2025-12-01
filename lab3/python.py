from flask import Flask, request, jsonify, make_response
from functools import wraps

app = Flask(__name__)


users = {
    "admin": "1234",
    "user": "password"
}

def check_auth(username, password):
    return username in users and users[username] == password

def authenticate():
    message = {"message": "Authentication required"}
    resp = make_response(jsonify(message), 401)
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

items = {
    1: {"name": "Laptop", "price": 1000, "color": "black"},
    2: {"name": "Mouse", "price": 25, "color": "gray"},
}

@app.route("/items", methods=["GET", "POST"])
@requires_auth
def items_handler():
    if request.method == "GET":
        return jsonify(items)

    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON body required"}), 400

        new_id = max(items.keys()) + 1 if items else 1
        items[new_id] = data

        return jsonify({"message": "Item created", "id": new_id}), 201


@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
@requires_auth
def item_handler(item_id):

    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404


    if request.method == "GET":
        return jsonify(items[item_id])

    if request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON body required"}), 400

        items[item_id].update(data)
        return jsonify({"message": "Item updated"})

    if request.method == "DELETE":
        del items[item_id]
        return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(port=8000)
