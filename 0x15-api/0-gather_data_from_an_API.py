#!/usr/bin/python3
'''
This Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        r = requests.get("{}users/{}".format(url, user))
        name = r.json().get("name")
        if name is not None:
            req = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            tasks = len(req)
            completedTask = []
            for t in req:
                if t.get("completed") is True:
                    completedTask.append(t)
            count = len(completedTask)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, tasks))
            for title in completedTask:
                print("\t {}".format(title.get("title")))
