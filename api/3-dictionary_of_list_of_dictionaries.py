#!/usr/bin/python3
"""export data in the JSON format"""
from requests import get
from json import dump


def export_tasks_to_json():
    url = "https://jsonplaceholder.typicode.com"

    users_response = get(f"{url}/users")
    todos_response = get(f"{url}/todos")

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to retrieve data from the API")
        return

    users = users_response.json()
    todos = todos_response.json()

    data = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        tasks = []

        for todo in todos:
            if todo["userId"] == int(user_id):
                task = {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                tasks.append(task)

        data[user_id] = tasks

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        dump(data, f)

    print("Data exported to todo_all_employees.json successfully.")


if __name__ == "__main__":
    export_tasks_to_json()
