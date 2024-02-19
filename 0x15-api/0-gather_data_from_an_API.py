#!/usr/bin/python3
""" Return informations using REST Api """

import requests
from sys import argv


def get_user_data(user_id):
    user_link = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_resp = requests.get(user_link)
    return user_resp.json()


def get_todo_data(user_id):
    todo_link = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todo_resp = requests.get(todo_link)
    return todo_resp.json()


def main():
    user_id = argv[1]

    user_data = get_user_data(user_id)
    todo_data = get_todo_data(user_id)

    tasks = 0
    done = 0
    completed = []

    for todo_item in todo_data:
        tasks += 1
        if todo_item["completed"]:
            completed.append(todo_item["title"])
            done += 1

    print(f"Employee {user_data['name']} is done with tasks({done}/{tasks}):")
    for task_title in completed:
        print(f"\t {task_title}")


if __name__ == "__main__":
    main()
