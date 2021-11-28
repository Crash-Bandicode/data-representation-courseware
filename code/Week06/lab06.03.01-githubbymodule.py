from github import Github
import requests
import json

#dont forget to remove the minus from the key
g = Github("ghp_qk7WGoJ0uvCY2DggoA1BZ5aZE7Rjlu2Uj00-s")

repo = g.get_repo("Crash-Bandicode/aprivateone")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentsOfFile = response.text
#print (contentsOfFile)

newContents = contentsOfFile + "More stuff \n"
#print (newContents)

#function:
# update_file(path, message, content, sha, branch=NotSet, comitter=NotSet, author=NotSet)

gitHubResponse=repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)

print (gitHubResponse)