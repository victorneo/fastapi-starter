import pytest
from models.users import hash_password, check_password



def test_hash_password():
    pw = '12345678'

    hashed = hash_password(pw)
    assert check_password(hashed.decode('utf8'), pw)
    assert not check_password(hashed.decode('utf8'), '1234')

