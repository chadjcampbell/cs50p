from um import count


def test_full_long_string():
    assert count(
        'Um, thanks, um, for the yummy um album, you umbral scrum um... bum?') == 4


def test_short():
    assert count('um?') == 1


def test_start():
    assert count('Um, thanks for the album.') == 1


def test_punctuation():
    assert count('Um, thanks, um...') == 2
