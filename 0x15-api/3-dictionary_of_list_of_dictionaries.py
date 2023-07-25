#!/usr/bin/python3
"""Module 0-gather_data_from_an_API.py"""

import json
from requests import get


def to_do():
    """Records all tasks from all employees"""
    all_usr = "https://jsonplaceholder.typicode.com/users"

    dummy = {}
    all_usr_pyt_obj = {}
    ls_dict = []
    file = "todo_all_employees.json"

    all_user_data = get(all_usr).json()

    for user in all_user_data:
        username = user["username"]
        id = user["id"]

        uid_todo = ("https://jsonplaceholder.typicode.com/users/{}/todos"
                    .format(id))
        uid_todo_data = get(uid_todo).json()

        for i in uid_todo_data:
            dummy["username"] = username
            dummy["task"] = i["title"]
            dummy["completed"] = i["completed"]
            ls_dict.append(dummy)
            dummy = {}

        all_usr_pyt_obj[str(id)] = ls_dict
        ls_dict = []

    with open(file, mode="w", newline="") as f:
        json.dump(all_usr_pyt_obj, f, indent=2)


if __name__ == "__main__":
    """Lauch the script"""
    to_do()
