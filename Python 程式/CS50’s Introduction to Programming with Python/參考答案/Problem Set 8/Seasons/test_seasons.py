# Implement, in a file called test_seasons.py, one or more functions that test your implementation of any
# unctions besides main in seasons.py thoroughly, each of whose names should begin with test_


import pytest

from datetime import date
from io import StringIO
from seasons import calculateAgeInMinutes, printAgeInMinutes


def test_calculateAgeInMinutesToday():
    today = date.today().isoformat()
    assert calculateAgeInMinutes(today) == 0


def test_calculateAgeInMinutesInvalidDate():
    with pytest.raises(SystemExit):
        calculateAgeInMinutes("invalid-date")


def test_printAgeInMinutes(monkeypatch):
    mock_output = StringIO()
    monkeypatch.setattr("sys.stdout", mock_output)

    minutes = 525600
    printAgeInMinutes(minutes)

    expected_output = "Five hundred twenty five thousand six hundred minutes\n"

    assert mock_output.getvalue() == expected_output


def test_printAgeInZeroMinutes(monkeypatch):
    mock_output = StringIO()
    monkeypatch.setattr("sys.stdout", mock_output)

    minutes = 0
    printAgeInMinutes(minutes)

    expected_output = "Zero minutes\n"

    assert mock_output.getvalue() == expected_output
