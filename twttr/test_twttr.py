from twttr import shorten


def test_shorten():
    assert shorten('n.nSeR0J3,1YqInA6nID3S!') == 'n.nSR0J3,1Yqn6nD3S!'
