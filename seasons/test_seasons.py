from seasons import minutes
from datetime import date

def test_minutes_1yr():
    assert(minutes(date.fromisoformat('2022-11-19'),date.fromisoformat('2023-11-19'))) == "Five hundred twenty-five thousand, six hundred minutes"

def test_minutes_2yrr():
    assert(minutes(date.fromisoformat('2021-11-19'),date.fromisoformat('2023-11-19'))) == "One million, fifty-one thousand, two hundred minutes"
    