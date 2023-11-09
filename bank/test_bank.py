from bank import value


def test_zero():
    assert value('hello, David') == 0
    assert value('HELLO, David') == 0


def test_twenty():
    assert value('hey, David') == 20
    assert value('HEY, David') == 20


def test_hundred():
    assert value('sup, David') == 100
    assert value('SUP, David') == 100
