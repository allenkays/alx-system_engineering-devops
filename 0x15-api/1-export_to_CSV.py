#!/usr/bin/python3
'''
This Python script that returns information using REST API
'''
import requests
import csv
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        r = requests.get("{}users/{}".format(url, user))
        name = r.json().get("username")
        if name is not None:
            req = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            tasks = []
            for t in req:
                task = {}
                task["USER_ID"] = user
                task["USERNAME"] = name
                task["TASK_COMPLETED_STATUS"] = t.get("completed")
                task["TASK_TITLE"] = t.get("title")
                tasks.append(task)
            with open("{}.csv".format(user), "w", newline="") as f:
                fieldnames = ["USER_ID", "USERNAME",
                              "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(tasks)
