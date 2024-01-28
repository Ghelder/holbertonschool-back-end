#!/usr/bin/python3
"""Export data to CSV"""
from requests import get
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    all_users = get(url=f"{URL}/todos", params={"userId": argv[1]}).json()
    users = get(url=f"{URL}/users/{argv[1]}").json()

    with open(f"{argv[1]}.csv", "w") as f:
        for i in all_users:
            userId = i.get("userId")
            name = users.get("username")
            completed = i.get("completed")
            title = i.get("title")
            f.write(f'"{userId}", "{name}", "{completed}", "{title}"\n')
