import pytest
from db import Database

@pytest.fixture
def db():
    """ Provided a fresh instance of a Database class and cleanup instance after the test """

    # Build up pre-requisites for running the test
    database = Database()
    yield database
    # Tear down the pre-requisites after the tests have been run
    database.data.clear()

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_duplicate_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None

