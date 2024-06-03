#!/usr/bin/python3
"""Gets data for a given employee ID"""
import requests
from sys import argv


def employee_name(employee_id):
    """Gets name of an employee for a given employee ID"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee = response.json()
    name = employee.get('name')
    return name


def employee_todos(employee_id):
    """Gets todos for a given employee ID"""
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)
    response = requests.get(url)
    todos = response.json()
    return todos


def main(employee_id):
    """Gets data for a given employee ID"""
    employee = employee_name(employee_id)
    todos = employee_todos(employee_id)
    completed = [todo for todo in todos if todo.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        employee, len(completed), len(todos)))
    [print('\t {}'.format(todo.get('title'))) for todo in completed]


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
    else:
        main(argv[1])
