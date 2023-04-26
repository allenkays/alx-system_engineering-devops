#!/usr/bin/python3
"""
A Python script that returns information using REST API
"""

import requests
import csv
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        r = requests.get("{}users/{}".format(url, user_id))
        name = r.json().get("name")

        if name is not None:
            req = requests.get(
                "{}todos?userId={}".format(
                    url, user_id)).json()
            tasks = len(req)
            completed_tasks = []
            for task in req:
                if task.get("completed") is True:
                    completed_tasks.append(task)
            count = len(completed_tasks)

            # Displaying the result in the required format
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, tasks))
            for title in completed_tasks:
                print("\t {}".format(title.get("title")))

            # Writing data to CSV file
            with open("{}{}.csv".format(user_id, name), 'w', newline='') as csvfile:
                taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for task in req:
                    taskwriter.writerow([user_id, name,
                                         task.get('completed'),
                                         task.get('title')])

