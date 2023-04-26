#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    # Process each user and their tasks
    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    # Output status messages
    print("All users found: OK")
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(todoAll, f)
    print("User ID and Tasks output: OK (file: {})".format(filename))

