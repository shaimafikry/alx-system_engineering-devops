#!/usr/bin/python3
"""
Training on using api from the virtual website typicode jsonplaceholder
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
        u_tasks = []
        comp_tasks = []
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
        t_u_tsks = len(u_tasks)
        for i in u_tasks:
            if i["completed"] is True:
                comp_tasks.append(i)
        # print (comp_tasks)
        t_comp_tsks = len(comp_tasks)
        # print (total_comp_tasks)
        print(f"Employee {name} is done with tasks({t_comp_tsks}/{t_u_tsks}):")
        for i in comp_tasks:
            task_name = i["title"]
            print("\t {}".format(task_name))
    else:
        print("Usage: missing id")
