import pytest
from src.app import create_app, db


@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():   
        db.create_all()
        yield app   # Note that we changed return for yield, see below for why
        db.session.remove()
        db.drop_all()
    return app