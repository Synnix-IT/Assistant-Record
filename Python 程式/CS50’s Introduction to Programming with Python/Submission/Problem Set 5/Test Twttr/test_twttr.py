from twttr import shorten

def test_Twttr() -> None:
    assert shorten("Twitter") == "Twttr"

def test_Whts() -> None:
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_CS50() -> None:
    assert shorten("CS50") == "CS50"

def test_PYTHON() -> None:
    assert shorten("PYTHON") == "PYTHN"




