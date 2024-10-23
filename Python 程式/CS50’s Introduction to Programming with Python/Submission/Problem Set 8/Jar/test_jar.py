import pytest
from jar import Jar


def test_initialization():
    # Test valid initialization with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test valid initialization with custom capacity
    jar = Jar(capacity = 10)
    assert jar.capacity == 10
    assert jar.size == 0

    # Test invalid initialization (negative capacity)
    with pytest.raises(ValueError):
        Jar(capacity = -1)

def test_str_representation():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar = Jar()
    assert str(jar) == ""

def test_deposit():
    jar = Jar(capacity = 10)

    # Valid deposit
    jar.deposit(5)
    assert jar.size == 5

    # Deposit that exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(capacity = 10)
    jar.deposit(5)

    # Valid withdrawal
    jar.withdraw(3)
    assert jar.size == 2

    # Withdrawal that exceeds current size
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_capacity_property():
    jar = Jar(capacity = 15)
    assert jar.capacity == 15

def test_size_property():
    jar = Jar(capacity = 10)
    jar.deposit(7)
    assert jar.size == 7
