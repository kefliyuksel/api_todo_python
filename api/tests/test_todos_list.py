from flask import json
from helpers.utils import create_many_todos

def test_get_todos(client):
    create_many_todos(client, 5)
    response = client.get("/todos")
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['count'] >= 5