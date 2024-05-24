#!/usr/bin/python3
"""
Training on using api from the virtual website typicode jsonplaceholder
"""


import requests
import sys
import json
if __name__ == "__main__":
    filename = "todo_all_employees.json"
    dict_all = {}
    rest_api = "https://jsonplaceholder.typicode.com"
    # add .json to bring the json format as dict
    # if not used output would be [response 200]
    users = requests.get(f"{rest_api}/users").json()
    # print (data)
    for i in users:
        id = i["id"]
        name = i["username"]
        dict_all[id] = []
        # access to tasks
        tasks = requests.get(f"{rest_api}/users/{id}/todos/").json()
        for task in tasks:
            # print (tasks)
            status = task.get("completed")
            # print (status)
            title = task.get("title")
            # print(title)
            record = {"username": name, "task": title, "completed": status}
            dict_all[id].append(record)
    with open(filename, "w") as file:
        json.dump(dict_all, file)
