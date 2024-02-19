#!/usr/bin/python3
""" Return informations using REST Api """

import csv
import requests
from sys import argv


def get_user_data(user_id):
    user_link = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    return requests.get(user_link).json()


def get_todo_data(user_id):
    todo_link = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    return requests.get(todo_link).json()


def export_to_csv(user_id, user_data, todo_data):
    user = user_data["username"]
    file_name = f"{user_id}.csv"

    with open(file_name, mode="w", newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo_item in todo_data:
            writer.writerow(
                    [user_id, user, todo_item['completed'], todo_item['title']]
                    )

    print(f"Data has been exported to {file_name}")


def main():
    user_id = argv[1]
    user_data = get_user_data(user_id)
    todo_data = get_todo_data(user_id)

    export_to_csv(user_id, user_data, todo_data)


if __name__ == "__main__":
    main()
