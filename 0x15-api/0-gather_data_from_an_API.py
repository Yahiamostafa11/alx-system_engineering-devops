#!/usr/bin/python3

import requests
import sys

if __name__=='_main_':
    imployed = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    url = url + '/' + imployed

    response = requests.get(url)
    imployed = response.json().get('username')

    todourl = url + '/todos'
    response = requests.get(todourl)
    tasks = response.json()
    completed = []

    for task in tasks:
        if task.get('completed') is True:
            completed.append(task)
            completed += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(imployed, len(completed), len(tasks)))

    for task in completed:
        print('\t {}'.format(task.get('title')))
        