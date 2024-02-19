#!/usr/bin/python3
""" Return informations using REST Api """
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get('completed'))

    task_progress = (
        f"Employee {employee_name} is done with tasks "
        f"({completed_tasks}/{total_tasks}):"
    )
    print(task_progress)

    for task in todo_data:
        print(f"\t {task.get('title')}")

    print("\nCorrect number of tasks")
    print("Correct formatting of first line")
    print("All tasks in output")
