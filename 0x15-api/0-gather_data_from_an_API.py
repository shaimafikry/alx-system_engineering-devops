#!/usr/bin/python3
"""
 training on using api
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
        total_u_tasks = len(u_tasks)
        for i in u_tasks:
            if i["completed"] == True:
                comp_tasks.append(i)
        # print (comp_tasks)
        total_comp_tasks = len(comp_tasks)
        # print (total_comp_tasks)
        print(f"Employee {name} is done with tasks({total_comp_tasks}/{total_u_tasks}):")
        for i in comp_tasks:
            task_name = i["title"]
            print("\t {}".format(task_name))
    else:
        print("Usage: missing id")