#!/usr/bin/python3

import urllib.request
import json
import sys

EMPLOYEE_API_URL = 'https://jsonplaceholder.typicode.com/users/{}'
TODO_API_URL = 'https://jsonplaceholder.typicode.com/todos?userId={}'

def get_employee_name(employee_id):
    """
    Given an employee ID, this function returns the name of the corresponding employee.

    Args:
    employee_id (int): The ID of the employee to retrieve the name of.

    Returns:
    str: The name of the employee with the given ID.
    """
    with urllib.request.urlopen(EMPLOYEE_API_URL.format(employee_id)) as response:
        employee_data = json.loads(response.read().decode())
        return employee_data['name']

def get_todo_list(employee_id):
    """
    Given an employee ID, this function returns the TODO list of the corresponding employee.

    Args:
    employee_id (int): The ID of the employee to retrieve the TODO list of.

    Returns:
    list: A list of dictionaries representing the TODO list of the employee with the given ID.
    """
    with urllib.request.urlopen(TODO_API_URL.format(employee_id)) as response:
        return json.loads(response.read().decode())

def display_todo_list_progress(employee_id):
    """
    Given an employee ID, this function retrieves the TODO list of the employee and displays the progress of the tasks.

    Args:
    employee_id (int): The ID of the employee to display the progress of the TODO list of.
    """
    employee_name = get_employee_name(employee_id)
    todo_list = get_todo_list(employee_id)

    total_tasks = len(todo_list)
    done_tasks = len([task for task in todo_list if task['completed']])

    print("Employee {} is done with tasks ({}/{}):".format(employee_name, done_tasks, total_tasks))

    for task in todo_list:
        if task['completed']:
            print("\t {}".format(task['title']))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Error: Invalid employee ID')
        sys.exit(1)

    display_todo_list_progress(employee_id)
