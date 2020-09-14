#!/usr/bin/python3
""" python script to export data to csv """
import json
import requests
from sys import argv


if __name__ == '__main__':
    """ execute """
    e_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(e_id)).json()
    utodo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(e_id)).json()

    with open('{}.json'.format(e_id), "w", newline="") as jfile:
        for task in utodo:
            json.dump({e_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            }]}, jfile)
