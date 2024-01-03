#!/usr/bin/python3
""" Gather data from an API """
import requests
import json
import sys


def get_data(id):
    """
    Get data from JSONPlacaholder API

    Args:
        id (int): Employee ID
    """
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    todo_res = requests.get(todo_url).json()

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user_res = requests.get(user_url).json()

    # Export data in the JSON format.
    data = {}
    data[id] = []
    for task in todo_res:
        data[id].append({"task": task.get("title"),
                         "completed": task.get("completed"),
                         "username": user_res.get("username")})

    with open(f"{id}.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    get_data(sys.argv[1])
