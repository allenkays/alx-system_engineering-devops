#!/usr/bin/python3
'''
This Python script that returns information using REST API
'''
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
            for t in req:
                if t.get("completed") is True:
                    completed_tasks.append(t)
            count = len(completed_tasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, tasks))
            for title in completed_tasks:
                print("\t {}".format(title.get("title")))

            with open(f"{user_id}.csv", "w", newline="") as csvfile:
                csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for t in req:
                    csv_writer.writerow(
                        [user_id, name, t.get("completed"), t.get("title")])
