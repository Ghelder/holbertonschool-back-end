#!/usr/bin/python3
"""export data in the JSON format"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    params = {"userId": int(argv[1])}
    res_user = get(f"{URL}/users", params=params).json()

    params = {"userId": int(argv[1])}
    res = get(f"{URL}/todos", params=params).json()

    tasks = []

    for x in res_user:
        name = x.get("name")

    for x in res:
        task = {
            "task": x.get("title"),
            "completed": x.get("completed"),
            "username": name,
        }
        tasks.append(task)

    data = {str(argv[1]): tasks}

    with open(f"{argv[1]}.json", "w", encoding="utf-8") as f:
        dump(data, f)
