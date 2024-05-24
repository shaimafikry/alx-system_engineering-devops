#!/usr/bin/python3
"""
Training on using api from the virtual website typicode jsonplaceholder
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        u_tasks = []
        comp_tasks = []
        filename = "{}.json".format(id)
        employ_dict = {}
        rest_api = "https://jsonplaceholder.typicode.com"
        # add .json to bring the json format as dict
        # if not used output would be [response 200]
        data = requests.get(f"{rest_api}/users/{id}").json()
        # print (data)
        name = data["username"]
        # print(name)
        tasks = requests.get(f"{rest_api}/todos/").json()
        for i in tasks:
            if i["userId"] == id:
                u_tasks.append(i)
        # print (u_tasks)
        for i in u_tasks:
            i.pop("userId")
            i.pop("id")
            i["username"] = name
        employ_dict[id] = u_tasks
        # print (employ_dict)
        with open(filename, "w") as file:
            data = json.dumps(employ_dict)
            file.write(data)
    else:
        print("Usage: missing id")
