#!/usr/bin/python3
""" Return informations using REST Api """
import json
import requests
from sys import argv

if __name__ == "__main__":

    user_link = f"https://jsonplaceholder.typicode.com/users"
    user_resp = requests.get(user_link)
    user_data = user_resp.json()

    all_data = {}

    for user_item in user_data:
        user = user_item["id"]
        todo_link = f"https://jsonplaceholder.typicode.com/users/{user}/todos"
        todo_resp = requests.get(todo_link)
        todo_data = todo_resp.json()

        username = user_item["username"]
        tasks = []
        for todo in todo_data:
            tasks.append(
                    {
                        "username": username,
                        "task": todo["title"],
                        "completed": todo["completed"]
                    })

        all_data[user] = tasks

    file_name = "todo_all_employees.json"
    with open(file_name, mode="w") as json_file:
        json.dump(all_data, json_file, indent=4)
