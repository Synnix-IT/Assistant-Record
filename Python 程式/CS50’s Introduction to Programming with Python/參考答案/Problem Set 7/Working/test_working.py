# Implement, in a file called test_working.py, three or more functions that
# collectively test your implementation of convert thoroughly, each of whose
# names should begin with test_


from working import convert
import pytest

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_format():
    with pytest.raises(ValueError):
        convert("9 to 5")
        convert("17:00 to 9 PM")
