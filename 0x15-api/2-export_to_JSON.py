#!/usr/bin/python3
"""Module 0-gather_data_from_an_API.py"""

import json
from requests import get
from sys import argv


def to_do(id):
    """Records all tasks that are owned by this employee"""
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    usr_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    dummy = {}
    usr_pyt_obj = {}
    ls_dict = []
    file = "{}.json".format(id)

    uid_user_data = get(usr_url).json()
    uid_todo_data = get(usr_todo).json()

    usr_username = uid_user_data["username"]

    for i in uid_todo_data:
        dummy["task"] = i["title"]
        dummy["completed"] = i["completed"]
        dummy["username"] = usr_username
        ls_dict.append(dummy)
        dummy = {}

    usr_pyt_obj[str(id)] = ls_dict
    with open(file, mode="w", newline="") as f:
        json.dump(usr_pyt_obj, f, indent=2)


if __name__ == "__main__":
    """Lauch the script"""
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    to_do(int(argv[1]))
