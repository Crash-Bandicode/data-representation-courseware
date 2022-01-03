from flask import Flask, url_for, request, redirect, abort, jsonify
from StockDAO import stockDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')



#curl Http://127.0.0.1:5000/
@app.route('/')
def index():
    return "hello"

#get all
#curl Http://127.0.0.1:5000/products
@app.route('/products')
def getAll():
    return jsonify(stockDAO.getAll())
# find By id

# curl Http://127.0.0.1:5000/products/1
@app.route('/products/<int:id>')
def findById(id):

    return jsonify(stockDAO.findByID(id))

# create
# λ curl -X POST -d "{\"name\":\"test\", \"price\": 123, \"quantity\": 4}" -H Content-Type:application/json http://127.0.0.1:5000/products
@app.route('/products', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    
    product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    return jsonify(stockDAO.create(product))


#update
# curl -X PUT -d "{\"id\": 5, \"name\":\"Updated Name\", \"price\": 123, \"quantity\": 4}" -H Content-Type:application/json http://127.0.0.1:5000/products/1
@app.route('/products/<int:id>', methods=['PUT'])
def update(id):
    foundProducts = stockDAO.findByID(id)
    print(foundProducts)
    if foundProducts == {}:
        return jsonify({}), 404
    currentProduct = foundProducts
    if 'name' in request.json:
        currentProduct['name'] = request.json['name']
    if 'price' in request.json:
        currentProduct['price'] = request.json['price']
    if 'Price' in request.json:
        currentProduct['quantity'] = request.json['quantity']
    stockDAO.update(currentProduct)

    return jsonify(currentProduct)

#delete
#  curl -X DELETE Http://127.0.0.1:5000/products/2
@app.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    stockDAO.delete(id)
    
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)