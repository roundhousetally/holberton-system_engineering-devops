#!/usr/bin/python3
""" python script to export data to csv """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    """ execute """
    e_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(e_id)).json()
    utodo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(e_id)).json()

    with open('{}.csv'.format(e_id), "w", newline="") as cfile:
        task_list = csv.writer(cfile, quoting=csv.QUOTE_ALL)
        for task in utodo:
            task_list.writerow([e_id, user.get('username'),
                                task.get('completed'), task.get('title')])
