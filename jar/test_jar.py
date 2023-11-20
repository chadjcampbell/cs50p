from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        _ = Jar(-1)
    jar = Jar()
    assert str(jar) == ""
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
