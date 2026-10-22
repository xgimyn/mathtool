import math

MAX_VALUE = 10000


def check_coefficients(coefficients):
    """Проверяет, что коэффициенты по модулю не превышают MAX_VALUE."""
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")


def solve(a, b, c):
    """Возвращает (вид уравнения, дискриминант, список корней)."""
    # Проверка диапазона коэффициентов
    check_coefficients({"A": a, "B": b, "C": c})

    # Проверка, является ли запись уравнением
    if a == 0 and b == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")

    # Линейное уравнение
    if a == 0:
        return "линейное", None, [-c / b]

    # Квадратное уравнение
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]
    else:
        return "квадратное", d, []
