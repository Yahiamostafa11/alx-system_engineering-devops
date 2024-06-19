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

    dictionary = {imployed: []}
    for task in tasks:
        dictionary[imployed].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(imployed), 'w') as filename:
        json.dump(dictionary, filename)