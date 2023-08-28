#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
from sys import argv
from requests import get

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    params = {"id": int(argv[1])}
    res_user = get(f"{URL}/users", params=params).json()
    for x in res_user:
        name = x.get("name")

    params = {"userId": int(argv[1])}
    res = get(f"{URL}/todos", params=params).json()

    val_task = [x for x in res if x.get("completed")]
    print(f"Employee {name} is done with tasks({len(val_task)}/{len(res)}):")
    for x in val_task:
        print(f'\t{x.get("title")}')
