#!/usr/bin/python3
"""Export data to JSON"""
from requests import get
from json import dumps
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    all_users = get(url=f"{URL}/todos", params={"userId": argv[1]}).json()
    users = get(url=f"{URL}/users/{argv[1]}").json()

    with open(f"{argv[1]}.json", "w") as f:
        json_dict = {}
        json_dict[argv[1]] = []
        for i in all_users:
            json_dict[argv[1]].append({
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": users.get("username")
            })
        f.write(dumps(json_dict))
