import sys
from calc import equation

# Проверка вызова справки или отсутствия аргументов
if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] == "--help"):
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print(f"Коэффициенты A, B, C — целые числа, по модулю не превышающие {equation.MAX_VALUE}.")
    sys.exit(0)

# Проверка, что первая команда - это solve
if sys.argv[1] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

# Получение строковых значений коэффициентов
if len(sys.argv) == 2:
    # Запуск только с командой solve -> ввод с клавиатуры
    a_str = input("Введите A: ")
    b_str = input("Введите B: ")
    c_str = input("Введите C: ")
elif len(sys.argv) == 8:
    # Запуск с аргументами: mathtool.py solve -a 1 -b 2 -c 3
    if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    a_str = sys.argv[3]
    b_str = sys.argv[5]
    c_str = sys.argv[7]
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)

# Преобразование строк в целые числа
try:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

# Решение уравнения через модуль calc.equation
try:
    kind, d, roots = equation.solve(a, b, c)
except ValueError as error:
    print(f"ОШИБКА: {error}", file=sys.stderr)
    sys.exit(1)

# Вывод результатов
if kind == "линейное":
    print("Уравнение линейное")
else:
    print("Уравнение квадратное")

if d is not None:
    print(f"D = {d}")

if len(roots) == 0:
    print("Действительных корней нет")
elif len(roots) == 1:
    print(f"x = {roots[0]:.3f}")
else:
    print(f"x1 = {roots[0]:.3f}")
    print(f"x2 = {roots[1]:.3f}")

sys.exit(0)
