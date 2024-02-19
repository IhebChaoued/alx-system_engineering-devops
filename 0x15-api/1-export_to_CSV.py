#!/usr/bin/python3
""" Return informations using REST Api """
import csv
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

    user = user_data["username"]

    file_name = f"{user_id}.csv"
    with open(file_name, mode="w", newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo_item in todo_data:
            writer.writerow(
                    [user_id, user, todo_item['completed'], todo_item['title']]
                    )
