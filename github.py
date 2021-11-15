import requests
import json

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+ username)
        return response.json()

    def getRepos(self, username):
        response = requests.get(self.api_url+"/users/"+ username+ "/repos")
        return response.json()


github = Github()

while True:
    choice = input("1- Find User\n2- Get Repositories\n3- Exit\nChoice: ")

    if choice == "3":
        break
    else:
        if choice == "1":
            username = input("Username: ")
            result = github.getUser(username)
            print(f"name: {result['name']}, public repos: {result['public_repos']}, followers: {result['followers']}, following: {result['following']}")
        elif choice == "2":
            username = input("username: ")
            result = github.getRepos(username)
            for repo in result:
                print(repo["name"])
        else:
            print("Invalid Choice")
