import pytest
from working import convert


def test_single_hourse():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'


def test_minutes():
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_bad_input():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')


def test_bad_hrs_or_mins():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
        convert('9:00 AM to 17:00 PM')
        convert('10:75 AM to 26:75 PM')
