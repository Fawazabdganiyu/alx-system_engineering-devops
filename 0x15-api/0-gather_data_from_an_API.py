#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


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

    total_tasks = len(todo_res)
    done_tasks = [task for task in todo_res if task.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".format(user_res.get('name'),
                                                          len(done_tasks),
                                                          total_tasks))

    for task in todo_res:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    get_data(argv[1])
