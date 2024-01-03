#!/usr/bin/python3
""" Gather data from an API """
import requests
import csv
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

    # Record "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE" to CSV
    with open(f"{id}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_res:
            writer.writerow([id,
                             user_res.get('username'),
                             task.get('completed'),
                             task.get('title')])


if __name__ == "__main__":
    get_data(sys.argv[1])
