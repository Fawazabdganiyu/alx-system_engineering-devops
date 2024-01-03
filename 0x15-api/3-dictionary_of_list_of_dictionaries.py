#!/usr/bin/python3
""" Gather data from an API """
import json
import requests


def get_data():
    """
    Get data from JSONPlacaholder API
    """
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_res = requests.get(user_url).json()

    # Export data for all employees in the JSON format.
    data = {}
    for user in user_res:
        user_id = user.get('id')

        todo = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todo_res = requests.get(todo).json()

        data[user_id] = []
        for task in todo_res:
            data[user_id].append({"username": user.get("username"),
                                  "task": task.get("title"),
                                  "completed": task.get("completed")})

    with open("todo_all_employees.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    get_data()
