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

    with open('{}.csv'.format(imployed), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(imployed, username, task.get('completed'),
                               task.get('title')))