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
