#!/usr/bin/python3
"""Module 0-gather_data_from_an_API.py"""
import requests
import sys


def to_do(num):
    """Returns the number of tasks for a given employee ID"""
    if type(num) == int:
        url_todo = "https://jsonplaceholder.typicode.com/todos"
        url_user = "https://jsonplaceholder.typicode.com/users"

        raw_todo = requests.get(url_todo).json()
        raw_user = requests.get(url_user).json()

        total_todo = 0
        complete = 0
        emp_name = ""
        cmp_title = []
        for i in raw_todo:
            if i["userId"] == num:
                total_todo += 1
                if i["completed"]:
                    complete += 1
                    cmp_title.append(i["title"])
        for j in raw_user:
            if j["id"] == num:
                emp_name = j["name"]
        print(("Employee {} is done with tasks({}/{}):".
               format(emp_name, complete, total_todo)))
        for k in cmp_title:
            print("\t {}".format(k))
    else:
        return


if __name__ == "__main__":
    to_do(int(sys.argv[1]))
