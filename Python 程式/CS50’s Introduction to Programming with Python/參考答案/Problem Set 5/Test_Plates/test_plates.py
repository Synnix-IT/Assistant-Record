# Implement four or more functions that collectively test your
# implementation of is_valid thoroughly, each of whose names should
# begin with test_ so that you can execute your tests.

from plates import is_valid


def test_startswith():
    assert is_valid("123456") == False
    assert is_valid("AA1234") == True
    assert is_valid("AA0123") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("AA123456") == False
    assert is_valid("CS50") == True


def test_punctuation():
    assert is_valid("!CS50") == False
    assert is_valid("CS, 50") == False


def test_format():
    assert is_valid("CS50AB") == False
    assert is_valid("AA123A") == False