#!/usr/bin/python3
"""This script to exports data in the json format"""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    uid = sys.argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(uid))
    name = url.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo = todos.json()
    taskList = []
    todo_All = {}
    for i in todo:
        if i.get('userId') == int(uid):
            dict = {"task": i.get('title'),
                    "completed": i.get('completed'),
                    "username": url.json().get('username')}
            taskList.append(dict)
    todo_All[uid] = taskList
    fileName = "{}.json".format(uid)
    with open(fileName, mode='w') as jsn:
        json.dump(todo_All, jsn)
