#!/usr/bin/python3
""" Export to JSON module"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user = requests.get(url+'users/'+argv[1]).json()
    todos = requests.get(f'{url}todos', params={"userId": userId}).json()
    completed = [todo.get('title') for todo in todos if todo.get('completed')]

    with open(f'{userId}.json', mode='w') as file:
        json.dump({
            userId: [
                {"task": todo.get('title'), "completed": todo.get('completed'),
                 "username": user.get('username')}
                for todo in todos
            ]
        }, file)
