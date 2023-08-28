#!/usr/bin/python3
"""export data in the CSV format"""
from requests import get
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    params = {"id": int(argv[1])}
    res_user = get(f"{URL}/users", params=params).json()

    params = {"userId": int(argv[1])}
    res = get(f"{URL}/todos", params=params).json()

    for x in res_user:
        name = x.get("username")
        for x in res:
            userId = x.get("userId")
            completed = x.get("completed")
            title = x.get("title")
            string = f'''"{userId}","{name}","{completed}","{title}"'''
            with open(f"{x.get('userId')}.csv", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
