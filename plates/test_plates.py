from plates import is_valid


def test_first_two_alpha():
    assert is_valid('AABBCC') == True
    assert is_valid('11BBCC') == False


def test_length():
    assert is_valid('A') == False
    assert is_valid('AABBCCDD') == False


def test_first_number_zero():
    assert is_valid('AABB01') == False


def test_digits_in_middle():
    assert is_valid('AABB11') == True
    assert is_valid('AA11BB') == False


def test_non_alphanum():
    assert is_valid('YEAH!') == False
