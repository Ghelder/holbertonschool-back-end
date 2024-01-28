#!/usr/bin/python3
"""using the API"""
from requests import get
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    all_users = get(url=f"{URL}/todos", params={"userId": argv[1]}).json()
    users = get(url=f"{URL}/users/{argv[1]}").json()
    name = users.get("name")

    num_tasks = [i for i in all_users if i.get("completed")]

    all_tasks = [i.get("completed") for i in all_users]
    print(f"Employee {name} is done with tasks({len(num_tasks)}/"
          f"{len(all_tasks)}):")

    for i in all_users:
        if i.get("completed"):
            print(f"\t {i.get('title')}")
