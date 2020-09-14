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
    allutasks = []
    # get all tasks for user first
    for task in utodo:
        tdict = {}
        tdict["task"] = task.get("title")
        tdict["completed"] = task.get("completed")
        tdict["username"] = user.get("username")
        allutasks.append(tdict)
    jsontsk = {}
    jsontsk[e_id] = allutasks
    with open('{}.json'.format(e_id), "w", newline="") as jfile:
        json.dump(jsontsk, jfile)
