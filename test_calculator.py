"""Модульные тесты класса Calculator (запуск: python3 -m pytest -v test_calculator.py)."""
import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    """Новый объект калькулятора для каждого теста."""
    return Calculator()


# ---------- add ----------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-3, 7, 4),
    (-3, -3, -6),
    (0, 0, 0),
    (2.5, 0.5, 3.0),
], ids=["positive", "negative_and_positive", "two_negative", "zeros", "floats"])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


def test_add_floats_precision(calc):
    # 0.1 + 0.2 в Python даёт 0.30000000000000004, поэтому сравниваем через approx
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


# ---------- subtract ----------
@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (0, 1, -1),
    (-3, 9, -12),
    (7, -12, 19),
    (5.5, 2.5, 3.0),
], ids=["positive", "result_negative", "negative_minus_positive", "minus_negative", "floats"])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# ---------- multiply ----------
@pytest.mark.parametrize("a, b, expected", [
    (6, 7, 42),
    (-2, 3, -6),
    (-4, -5, 20),
    (0, 15, 0),
    (2, 4.5, 9.0),
], ids=["positive", "one_negative", "two_negative", "by_zero", "float"])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# ---------- divide ----------
@pytest.mark.parametrize("a, b, expected", [
    (28, 8, 3.5),
    (9, 3, 3),
    (-10, 4, -2.5),
    (0, 10, 0),
], ids=["fraction_result", "integer_result", "negative", "zero_dividend"])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


@pytest.mark.parametrize("a", [5, -5, 0, 2.5])
def test_divide_by_zero_raises_exception(calc, a):
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calc.divide(a, 0)


# ---------- power ----------
@pytest.mark.parametrize("base, exponent, expected", [
    (2, 5, 32),
    (2, 0, 1),
    (2, -1, 0.5),
    (-3, 3, -27),
    (9, 0.5, 3.0),
], ids=["positive", "zero_exponent", "negative_exponent", "negative_base", "fractional_exponent"])
def test_power(calc, base, exponent, expected):
    assert calc.power(base, exponent) == expected


def test_power_zero_to_negative_raises_exception(calc):
    with pytest.raises(ZeroDivisionError):
        calc.power(0, -2)


# ---------- square_root ----------
@pytest.mark.parametrize("x, expected", [
    (25, 5),
    (0, 0),
    (2.25, 1.5),
], ids=["perfect_square", "zero", "float"])
def test_square_root(calc, x, expected):
    assert calc.square_root(x) == expected


def test_square_root_irrational(calc):
    assert calc.square_root(2) == pytest.approx(1.41421356)


def test_square_root_negative_raises_exception(calc):
    with pytest.raises(ValueError, match="Корень из отрицательного числа"):
        calc.square_root(-4)


# ---------- is_prime_number ----------
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (17, True),
    (97, True),
    (1, False),
    (0, False),
    (-7, False),
    (4, False),
    (9, False),
    (100, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) is expected


def test_is_prime_number_float_raises_exception(calc):
    with pytest.raises(TypeError):
        calc.is_prime_number(7.5)


# ---------- проверка типов ----------
@pytest.mark.parametrize("method", ["add", "subtract", "multiply", "divide", "power"])
def test_methods_reject_strings(calc, method):
    with pytest.raises(TypeError, match="Ожидалось число"):
        getattr(calc, method)("5", 2)
