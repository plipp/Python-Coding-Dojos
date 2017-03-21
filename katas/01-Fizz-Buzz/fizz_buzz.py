# actual code
def fizz_buzz(number):
    result = ""
    if number % 3 == 0:
        result = "fizz"
    if number % 5 == 0:
        result += "buzz"
    if result == "":
        result = number
    return result


def test_buzz():
    assert fizz_buzz(55) == 'buzz'


def test_fizzbuzz():
    assert fizz_buzz(150) == 'fizzbuzz'


# tests
def test_fizz_buzz():
    assert fizz_buzz(1) == 1


def test_fizz_buzz_2():
    assert fizz_buzz(3) == "fizz"
