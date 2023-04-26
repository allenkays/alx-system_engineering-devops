#!/usr/bin/python3
"""
This script returns information on an employees todo list
using REST API
"""

import requests
import sys

EMPLOYEE_API_URL = 'https://jsonplaceholder.typicode.com/users/{}'
TODO_API_URL = 'https://jsonplaceholder.typicode.com/todos?userId={}'

def get_employee_name(employee_id):
    response = requests.get(EMPLOYEE_API_URL.format(employee_id))
    employee_data = response.json()
    return employee_data['name']

def get_todo_list(employee_id):
    response = requests.get(TODO_API_URL.format(employee_id))
    return response.json()

def display_todo_list_progress(employee_id):
    employee_name = get_employee_name(employee_id)
    todo_list = get_todo_list(employee_id)

    total_tasks = len(todo_list)
    done_tasks = len([task for task in todo_list if task['completed']])

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))

    for task in todo_list:
        if task['completed']:
            print("\t- {}".format(task['title']))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Error: Invalid employee ID')
        sys.exit(1)
