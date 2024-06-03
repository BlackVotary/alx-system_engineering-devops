#!/usr/bin/python3
"""Exports data in the JSON format"""
import json
from sys import argv

import requests


def get_username(employee_id):
    """Gets username of an employee for a given employee ID"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee = response.json()
    username = employee.get('username')
    return username


def get_todos(employee_id):
    """Gets todos for a given employee ID"""
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)
    response = requests.get(url)
    todos = response.json()
    return todos


def write_json(employee_id, username, todo_list):
    """Writes data to a JSON file"""
    tasks = [{"task": task["title"], "completed": task["completed"],
              "username": username} for task in todo_list]
    data = {str(employee_id): tasks}
    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def main(employee_id):
    """Exports data in the CSV format"""
    username = get_username(employee_id)
    todos = get_todos(employee_id)
    write_json(employee_id, username, todos)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
    else:
        try:
            employee_id = int(argv[1])
            main(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
