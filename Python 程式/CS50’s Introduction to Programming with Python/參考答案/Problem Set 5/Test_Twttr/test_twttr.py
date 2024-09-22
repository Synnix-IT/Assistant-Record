# Implement one or more functions that collectively test your
# implementation of shorten thoroughly

from twttr import shorten


def test_allUpper() -> None:
    assert shorten("WORD") == "WRD"

def test_allLower() -> None:
    assert shorten("word") == "wrd"

def test_upperAndLower() -> None:
    assert shorten("WorD") == "WrD"

def test_number() -> None:
    assert shorten("1234") == "1234"

def test_punctuation() -> None:
    assert shorten(".!?,") == ".!?,"
