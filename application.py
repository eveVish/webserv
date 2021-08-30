import flask
from flask import Flask
from flask_pymongo import PyMongo
from parameters import pr_id, product_name, product_description, prod_color, product_size

app = Flask(__name__)

mongodb_client = PyMongo(app, uri='mongodb://localhost:27017/Products_db')
db = mongodb_client.db

products = db.products


@app.route('/add', methods=['POST', 'GET'])
def add_product():
    """Дабавляет товар в базу данных."""
    db.products.insert_one({'_id': pr_id,
                            'name': product_name,
                            'description': product_description,
                            'color': prod_color,
                            'size': product_size}),
    return flask.jsonify(message="Product successfully added")


@app.route('/details/<int:id>', methods=['GET'])
def info(id):
    product_info = db.products.find_one({"_id": id})
    return product_info


@app.route('/sort', methods=['GET'])
def sort():
    prod = db.products.find()
    return flask.jsonify([products for products in prod])


@app.route('/sort/<product_name>', methods=['GET'])
def sort_by_name(product_name):
    pr = db.products.find({"name": product_name}).sort('name')
    return flask.jsonify([products for products in pr])


@app.route('/sort/param', methods=['GET'])
def sort_by_param():
    result = db.products.find({'param': "parameter_name"})
    return flask.jsonify([products for products in result])
