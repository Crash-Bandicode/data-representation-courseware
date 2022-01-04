from StockDAO import stockDAO

Product = {
    'id': 1,
    'name': 'Coke Can',
    'price': 1.10,
    'quantity': 300
}

Product2 = {
    'name': 'Milk',
    'price': 1.80,
    'quantity': 400
}


# Create
# returnValue = stockDAO.create(Product)
# print(returnValue)

# #GetAll:
returnValue = stockDAO.getAll()
print(returnValue)

# returnValue = stockDAO.findByID(Product2['id'])
# print(returnValue)
# print("findByID")

# returnValue = stockDAO.update(Product2)
# print(returnValue)


# returnValue = stockDAO.delete(2)
# print(returnValue)