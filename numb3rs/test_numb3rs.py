import pytest
from numb3rs import validate


def test_validate_works():
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('127.0.0.1') == True


def test_catches_value_error():
    assert validate('a.a.a.a') == False


def test_reject_out_of_bounds():
    assert validate('1.1.1.256') == False


def test_reject_any_missing_dots():
    assert validate('cat') == False
    assert validate('1.1.1') == False
    assert validate('c.1') == False
