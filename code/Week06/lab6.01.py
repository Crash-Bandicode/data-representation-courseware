import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#output to console
print (data) 

#output all cars individually
for car in data["cars"]:
    print (car)

#write returned JSON to file
filename = 'cars.json'
if filename:
    #writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# write cars to an excel file
w = Workbook()
ws = w.add_sheet('cars')
row = 0;
ws.write(row, 0, "reg")
ws.write(row, 1, "make")
ws.write(row, 2, "model")
ws.write(row, 3, "price")
row += 1
for car in data["cars"]:
    ws.write(row, 0, car["reg"])
    ws.write(row, 1, car["make"])
    ws.write(row, 2, car["model"])
    ws.write(row, 3, car["price"])
    row += 1
w.save('cars.xls')

#create a car on the server using the API
url2 = 'http://127.0.0.1:5000/cars'
dataString = {'reg':'08 C 1891', 'make':'Ford', 'model':'Galaxy', 'price':1234}
response2 = requests.post(url, json=dataString)

print (response2.status_code)

#Write response that updates car
url3 = 'http://127.0.0.1:5000/cars/test'
dataString = {'make':'Ford', 'model':'Kuga'}
response3 = requests.put(url3, json=dataString)

print (response3.status_code)
print (response.text)

#write a program that deletes a car from the server using the API
url4 = 'http://127.0.0.1:5000/cars/08%20C%201891'
response4 = requests.delete(url4)
print (response4.status_code)
print (response4.text)



