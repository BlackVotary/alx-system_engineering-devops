#!/usr/bin/python3
"""Exports data in the JSON format"""
import json

import requests


def get_all_employees():
    """Gets information of all employees"""
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    response = response.json()
    return response


def get_todos(employee_id):
    """Gets todos for a given employee ID"""
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)
    response = requests.get(url)
    todos = response.json()
    return todos


def write_json(all_data, filename="file.json"):
    """Writes data to a JSON file"""
    with open(filename, 'w') as jsonfile:
        json.dump(all_data, jsonfile, indent=4)


def main():
    """Exports data in the CSV format"""
    all_data = {}
    for employee in get_all_employees():
        employee_id = employee['id']
        username = employee['username']
        todos = get_todos(employee_id)
        tasks = [{"task": task["title"], "completed": task["completed"],
                  "username": username} for task in todos]
        all_data[str(employee_id)] = tasks

    write_json(all_data, "todo_all_employees.json")


if __name__ == '__main__':
    main()
