import mysql.connector
import config as cfg

class StockDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )


    def create(self, product):
        cursor = self.db.cursor()
        sql="insert into stock (name, price, quantity) values(%s,%s,%s)"
        values = [
            product["name"],
            product["price"],
            product["quantity"]
            ]
        cursor.execute(sql, values)
        self.db.commit()
        print("1 record inserted, ID", cursor.lastrowid)






    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from stock"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultsAsDict = self.convertToDict(result)
            returnArray.append(resultsAsDict)
        return returnArray


    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from stock where id = %s"
        values = [ id ]
        cursor.execute(sql, values)
        results = cursor.fetchone()
        return self.convertToDict(results)


    def update(self, product):
        cursor = self.db.cursor()
        sql="update stock set name=%s, price=%s, quantity=%s where id=%s"
        values = [
            product["name"],
            product["price"],
            product["quantity"],
            product["id"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return product



    def delete(self, id):
        cursor = self.db.cursor()
        sql="DELETE from stock WHERE id = %s"
        values = [ id ]
        cursor.execute(sql, values)
        print("id: " + str(id) + " Deleted")

    # Convert tuple to dict object:
    def convertToDict(self, result):
        colnames = ['id', 'name', 'price', 'quantity']
        product = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                product[colname] = value
        return product

stockDAO = StockDAO()