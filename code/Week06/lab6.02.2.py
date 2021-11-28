import requests
import json

url = 'https://api.github.com/repos/Crash-Bandicode/aprivateone'

apiKey = "ghp_qk7WGoJ0uvCY2DggoA1BZ5aZE7Rjlu2Uj00-s"
response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
#print(response.json())

file = open("lab06.02.2.aprivateone.html", 'w')
json.dump(repoJSON, file, indent=4)