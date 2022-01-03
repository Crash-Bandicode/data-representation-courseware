from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all
@app.route('/products')
def getAll():
    return jsonify(products)
# find By id
@app.route('/products/<int:id>')
def findById(id):

    return jsonify({})

# create
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/products', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    
    product = {
        "id": request.json["id"],
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    return jsonify({})


    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/products/<int:id>', methods=['PUT'])
def update(id):
    foundProducts = []
    if len(foundProducts) == 0:
        return jsonify({}), 404
    currentProduct = foundProducts[0]
    if 'Title' in request.json:
        currentProduct['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentProduct['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentProduct['Price'] = request.json['Price']

    return jsonify(currentProduct)

#delete
# curl -X DELETE http://127.0.0.1:5000/products/1
@app.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)