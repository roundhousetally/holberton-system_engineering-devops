#!/usr/bin/python3
""" python script to extract data using api """
import requests
from sys import argv


if __name__ == '__main__':
    """ execute """
    e_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(e_id)).json()
    utodo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(e_id)).json()

    ename = user.get('name')
    task_count = 0
    task_list = []
    completed_task = 0
    for task in utodo:
        task_count += 1
        if task.get('completed') is True:
            task_list.append(task)
            completed_task += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(ename, completed_task, task_count))
    for task in task_list:
        print('\t {}'.format(task.get('title')))
