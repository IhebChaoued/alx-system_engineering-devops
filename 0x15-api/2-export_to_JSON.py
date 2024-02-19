#!/usr/bin/python3
""" Return informations using REST Api """
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    todo_link = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_link = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    user_resp = requests.get(user_link)
    todo_resp = requests.get(todo_link)

    user_data = user_resp.json()
    todo_data = todo_resp.json()

    username = user_data["username"]

    tasks = []
    for todo in todo_data:
        tasks.append(
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": username}
                )

    json_data = {
        user_id: tasks
    }

    file_name = f"{user_id}.json"
    with open(file_name, mode="w") as json_file:
        json.dump(json_data, json_file, indent=4)
