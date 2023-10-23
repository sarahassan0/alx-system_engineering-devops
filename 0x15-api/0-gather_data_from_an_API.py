#!/usr/bin/python3
""" Gather data from an API module"""

import requests
from sys import argv

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]

    user = requests.get(url+'users/'+userId).json()
    todos = requests.get(f'{url}todos?userId={userId}').json()
    completed = [todo.get('title') for todo in todos if todo.get('completed')]

    print(f'Employee {user.get("name")} is done with tasks'
          f'({len(completed)}/{len(todos)}):')
    for todo in completed:
        print('\t ' + todo)
