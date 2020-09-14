#!/usr/bin/python3
""" python script to export data to csv """
import json
import requests


if __name__ == '__main__':
    """ execute """
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    utodo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    allutasks = {}
    user = {}
    for u in users:
        e_id = u.get('id')
        allutasks[e_id] = []
        user[e_id] = u.get('username')

    for task in utodo:
        tdict = {}
        e_id = task.get('userId')
        tdict["task"] = task.get("title")
        tdict["completed"] = task.get("completed")
        tdict["username"] = user.get(e_id)
        allutasks.get(e_id).append(tdict)

    with open('todo_all_employees.json', "w", newline="") as jfile:
        json.dump(allutasks, jfile)
