import pytest
from fuel import convert, gauge


def test_x_int():
    with pytest.raises(ValueError):
        convert('a/4')


def test_y_int():
    with pytest.raises(ValueError):
        convert('3/a')


def test_out_of_bounds():
    with pytest.raises(ValueError):
        convert('4/3')
        convert('-4/3')
        convert('4/-3')
        convert('1.5/3')


def test_int_errors():
    with pytest.raises(ValueError):
        convert('4/3')
        convert('-4/3')
        convert('4/-3')
        convert('1.5/3')
        convert('a/4')
        convert('3/a')
        convert('a/a')


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')


def test_gauge_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'


def test_gauge_empty():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'


def test_gauge_percents():
    assert gauge(25) == '25%'
    assert gauge(50) == '50%'
    assert gauge(75) == '75%'
