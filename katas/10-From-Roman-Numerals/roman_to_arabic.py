TABLE = dict(
    I=1,
    V=5,
    X=10,
    L=50,
    C=100,
    D=500,
    M=1000
)


def to_arabic(roman: str) -> int:
    if roman == '':
        return 0

    l = [TABLE[i] for i in roman]
    m_idx = l.index(max(l))

    return l[m_idx] - to_arabic(roman[:m_idx]) + to_arabic(roman[m_idx+1:])


def test_i():
    assert to_arabic('I') == 1


def test_roman_ii():
    assert to_arabic('II') == 2


def test_iv():
    assert to_arabic('IV') == 4


def test_xlii():
    assert to_arabic('XLII') == 42


def test_mmxiii():
    assert to_arabic('MMXIII') == 2013


def test_xcix():
    assert to_arabic('XCIX') == 99


def test_zero():
    assert to_arabic('') == 0
