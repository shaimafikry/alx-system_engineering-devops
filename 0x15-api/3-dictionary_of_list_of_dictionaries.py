#!/usr/bin/python3
"""
Training on using api from the virtual website typicode jsonplaceholder
"""


import requests
import sys
import json
if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
        u_tasks = []
        comp_tasks = []
        filename = "todo_all_employees.json"
        rest_api = "https://jsonplaceholder.typicode.com"
        # add .json to bring the json format as dict
        # if not used output would be [response 200]
        data = requests.get(f"{rest_api}/users/{id}").json()
        # print (data)
        name = data["name"]
        # print(name)
        tasks = requests.get(f"{rest_api}/todos/").json()
        # print (tasks)
        with open (filename,"w") as file:
            data = json.dumps(tasks)
            file.write(data)
    else:
        print("Usage: missing id")     