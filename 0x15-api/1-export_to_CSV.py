#!/usr/bin/python3
"""
Training on using api from the virtual website typicode jsonplaceholder
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        u_tasks = []
        filename = "USER_ID.csv"
        rest_api = "https://jsonplaceholder.typicode.com"
        # add .json to bring the json format as dict
        # if not used output would be [response 200]
        data = requests.get(f"{rest_api}/users/{id}").json()
        # print (data)
        name = data["name"]
        # print(name)
        tasks = requests.get(f"{rest_api}/todos/").json()
        for i in tasks:
            if i["userId"] == id:
                i["name"] = name
                u_tasks.append(i)
        # print (u_tasks)
        fields = ["userId", "name", "completed", "title"]
        with open(filename, "w", newline='') as csvfile:
            data = csv.DictWriter(csvfile, fieldnames=fields)
            for d in u_tasks:
                data.writerow({k: v for k, v in d.items() if k in fields})
    else:
        print("Usage: missing id")
