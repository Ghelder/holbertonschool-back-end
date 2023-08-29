#!/usr/bin/python3
"""export data in the JSON format"""
from json import dump
from requests import get


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    users_response = get(f"{URL}/users")
    todos_response = get(f"{URL}/todos")

    users = users_response.json()
    todos = todos_response.json()

    data = {}

    for user in users:
        USER_ID = str(user["id"])
        username = user["username"]
        tasks = []

        for todo in todos:
            if todo["userId"] == int(USER_ID):
                task = {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                tasks.append(task)

        data[USER_ID] = tasks

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        dump(data, f)
