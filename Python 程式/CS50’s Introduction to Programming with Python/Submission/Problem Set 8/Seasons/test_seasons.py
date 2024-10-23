import pytest

from datetime import date
from io import StringIO
from seasons import checkDays, printMinutes


def test_calculateAgeInMinutesToday():
    today = date.today().isoformat()
    assert checkDays(today) == 0


def test_calculateAgeInMinutesInvalidDate():
    with pytest.raises(SystemExit):
        checkDays("invalid-date")


def test_printAgeInMinutes(monkeypatch):
    mock_output = StringIO()
    monkeypatch.setattr("sys.stdout", mock_output)

    minutes = 525600
    printMinutes(minutes)

    expected_output = "Five hundred twenty-five thousand, six hundred minutes\n"

    assert mock_output.getvalue() == expected_output


def test_printAgeInZeroMinutes(monkeypatch):
    mock_output = StringIO()
    monkeypatch.setattr("sys.stdout", mock_output)

    minutes = 0
    printMinutes(minutes)

    expected_output = "Zero minutes\n"

    assert mock_output.getvalue() == expected_output
