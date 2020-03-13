from flask import json
from helpers.utils import create_todo

def test_create_todo(client):
    todo = {
        'title': 'todo test',
        'description': 'todo test description'
    }        
    response = client.post(
        '/todos',
        data=json.dumps(todo),
        content_type='application/json',
    )
    assert response.status_code == 201

def test_get_todo(client):
    todo = create_todo(client)
    response = client.get(
        '/todos/' + str(todo['id'])
    )
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['id'] == todo['id']
    assert data['title'] == todo['title']
    assert data['description'] == todo['description']

def test_update_todo(client):
    todo = create_todo(client)
    todo['title'] = 'test title updated'
    todo['description'] = 'test description updated'
    response = client.put(
        '/todos/' + str(todo['id']),
        data=json.dumps(todo),
        content_type='application/json',
    )
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['id'] == todo['id']
    assert data['title'] == todo['title']
    assert data['description'] == todo['description']

def test_delete_todo(client):
    todo = create_todo(client)
    response = client.delete(
        '/todos/' + str(todo['id'])
    )
    assert response.status_code == 204