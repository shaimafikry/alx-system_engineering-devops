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
        comp_tasks = []
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
                u_tasks.append(i)
        # print (tasks)
        # print (u_tasks)
        total_u_tasks = len(u_tasks)
        fields = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
        with open (filename,"w", newline='') as csvfile:
            data = csv.DictWriter(csvfile, fieldnames=fields)
            # data.header()
            data.rows(u_tasks)
    else:
        print("Usage: missing id")  
