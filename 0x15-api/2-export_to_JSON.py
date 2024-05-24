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
        filename = "{}.json".format(id)
        employ_dict = {id: []}
        rest_api = "https://jsonplaceholder.typicode.com"
        # add .json to bring the json format as dict
        # if not used output would be [response 200]
        data = requests.get(f"{rest_api}/users/{id}").json()
        # print (data)
        name = data["username"]
        # print(name)
        # get the user tasks directly
        tasks = requests.get(f"{rest_api}/users/{id}/todos/").json()
        # print(tasks)
        for i in tasks:
            title = i.get("title")
            status = i.get("completed")
            employ_dict[id].append({
                                   "task": title,
                                   "completed": status,
                                   "username": name})
        # print (employ_dict)
        with open(filename, "w") as file:
            json.dump(employ_dict, file)
    else:
        print("Usage: missing id")
