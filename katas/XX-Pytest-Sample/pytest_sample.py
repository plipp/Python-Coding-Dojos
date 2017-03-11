# test with: python -m pytest pytest_sample.py

def do_something():
    return 999


def test_do_something():
    assert do_something() == 99
