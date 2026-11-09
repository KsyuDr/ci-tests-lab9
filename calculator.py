"""Класс Calculator с бизнес-логикой калькулятора из ЛР1."""
import math


class Calculator:
    @staticmethod
    def _check_numbers(*values):
        """Проверяет, что все аргументы — числа (int или float, но не bool)."""
        for value in values:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"Ожидалось число, получено: {value!r}")

    def add(self, a, b):
        self._check_numbers(a, b)
        return a + b

    def subtract(self, a, b):
        self._check_numbers(a, b)
        return a - b

    def multiply(self, a, b):
        self._check_numbers(a, b)
        return a * b

    def divide(self, a, b):
        self._check_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def power(self, base, exponent):
        self._check_numbers(base, exponent)
        if base == 0 and exponent < 0:
            raise ZeroDivisionError("Ноль нельзя возводить в отрицательную степень")
        return base ** exponent

    def square_root(self, x):
        self._check_numbers(x)
        if x < 0:
            raise ValueError("Корень из отрицательного числа не существует")
        return math.sqrt(x)

    def is_prime_number(self, n):
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("Проверять на простоту можно только целые числа")
        if n < 2:
            return False
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True
