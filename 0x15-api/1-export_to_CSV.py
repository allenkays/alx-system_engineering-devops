#!/usr/bin/python3
"""
Export employee TODO list progress in CSV format using REST API.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    # Get user ID from command line arguments
    uid = argv[1]

    # Fetch user data from API
    user_url = f"https://jsonplaceholder.typicode.com/users/{uid}"
    user = requests.get(user_url).json()

    # Fetch TODO data from API
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"
    todo = requests.get(todo_url).json()

    # Write data to CSV file
    filename = f"{uid}.csv"
    with open(filename, 'w', newline='') as csvfile:
        # Use csv.writer to write rows to the file
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            # Write a row with four columns:
            # USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE
            taskwriter.writerow([int(uid), user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])
