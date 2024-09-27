from bank import value

def test_hello() -> None:
    assert value("Hello") == 0


def test_hello2() -> None:
    assert value(" Hello ") == 0


def test_helloMan() -> None:
    assert value("Hello, Newman") == 0


def test_howDoing() -> None:
    assert value("How you doing?") == 20


def test_whatHappen() -> None:
    assert value("What's happening?") == 100


def test_whatUp() -> None:
    assert value("What's up?") == 100


