import random
import string
from flask import json

def __randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def create_todo(client, title='', description=''):
    if not title:
        title = __randomString()
    if not description:
        description = __randomString()
        todo = {
            'title': title,
            'description': description
        }        
        response = client.post(
            '/todos',
            data=json.dumps(todo),
            content_type='application/json',
        )
        todo = json.loads(response.get_data(as_text=True))
        return todo

def create_many_todos(client, count=1):
    todos = []
    for i in range(count):
        todo = create_todo(client)
        todos.append(todo)
    return todos        