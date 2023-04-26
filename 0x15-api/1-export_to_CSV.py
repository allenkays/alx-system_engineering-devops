#!/usr/bin/python3
"""
This module contains a script that exports user tasks to a CSV file.

The script takes a user ID as an argument, retrieves the user's information and tasks
from a REST API, and saves them in a CSV file with the format "USER_ID.csv". Each row in
the CSV file contains information about a single task, including the task's completion
status, title, and the user's ID and username.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    """
    Entry point of the script.
    """
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
        """
        Write task data to CSV file.
        
        Each row in the CSV file contains information about a single task, including 
        the task's completion status, title, and the user's ID and username.
        """
        # Use csv.writer to write rows to the file
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            # Write a row with four columns:
            # USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE
            taskwriter.writerow([int(uid), user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])

