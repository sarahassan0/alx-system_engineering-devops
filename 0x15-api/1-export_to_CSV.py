#!/usr/bin/python3
""" Export to CSV module"""

import csv
import requests
from sys import argv

if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user = requests.get(url+'users/'+userId).json()
    todos = requests.get(f'{url}todos', params={"userId": userId}).json()
    completed = [todo.get('title') for todo in todos if todo.get('completed')]

    with open(f'{userId}.csv', mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([userId, user.get('username'),
                            todo.get('completed'), todo.get('title')])
