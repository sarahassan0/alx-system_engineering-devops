#!/usr/bin/python3
""" Export to JSON format"""

import json
import requests

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url+'users').json()
    todos = requests.get(url + "todos").json()

    employees_tasks = {}
    for user in users:
        userId = user.get('id')
        employee_tasks_list = []
        for todo in todos:
            if todo.get('userId') == userId:
                employees_tasks[userId] = [
                        {"username": user.get('username'),
                            "task": todo.get('title'),
                            "completed": todo.get('completed')}
                        for todo in todos
                    ]

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(employees_tasks, file)
