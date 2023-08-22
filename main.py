import json
import uuid

from flask import Flask, request, Response

from crud.users_crud import Users
from database import create_database
from exceptions import ValidationError
from models.user import User

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {
        "message": "Hello world"
    }


# API endpoints Users
# Get all users
@app.route("/users", methods=["GET"])
def get_all_users():
    users_crud = Users()

    try:
        users = users_crud.read()
    except Exception as exc:
        return Response(response=f"Server error: {exc}", status=500)
    if users:
        return Response(response=json.dumps(users), status=200)
    return Response(response=f"No users found in DB", status=404)


# Get user by id
@app.route("/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    pass


# Add user
@app.route("/users/add", methods=["POST"])
def add_user():
    user_data = json.loads(request.data) # json -> dict

    # cream un id pentru noul user
    new_id = str(uuid.uuid4())
    user_data["id"] = new_id

    try:
        user_obj = User(**user_data)
        # user_obj = User(id=user_data["id"], password=user_data["password"], ...)
        user_obj.validate()
    except ValidationError:
        return Response(response="User validation error", status=400)
    except Exception as e:
        return Response(response=f"User creation error, {e}", status=400)

    users_crud = Users()
    try:
        users_crud.create(user_obj)
    except Exception as e:
        return Response(response=f"Server error: {e}", status=500)

    return Response(response=json.dumps(user_data), status=201)

# Update user
@app.route("/users/update/<user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    pass


# Delete user
@app.route("/users/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    pass


# API endpoints Products
# Get all products
@app.route("/products", methods=["GET"])
def get_all_products():
    pass


# Get product by id
@app.route("/products/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    pass


# Add product
@app.route("/products/add", methods=["POST"])
def add_product():
    pass


# Update product
@app.route("/products/update/<product_id>", methods=["PUT", "PATCH"])
def update_product(product_id):
    pass


# Delete product
@app.route("/products/delete/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    pass


# API endpoints Orders
# Get all orders
@app.route("/orders", methods=["GET"])
def get_all_orders():
    pass


# Get order by id
@app.route("/orders/<order_id>", methods=["GET"])
def get_order_by_id(order_id):
    pass


# Add order
@app.route("/orders/add", methods=["POST"])
def add_order():
    pass


# Update order
@app.route("/orders/update/<order_id>", methods=["PUT", "PATCH"])
def update_order(order_id):
    pass


# Delete order
@app.route("/orders/delete/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    pass


if __name__ == "__main__":
    create_database()
    app.run(debug=True, port=7000)
