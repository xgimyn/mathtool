import math
import sys
MAX_VALUE = -5
if MAX_VALUE < 0:
    MAX_VALUE = MAX_VALUE * -1
# Проверка вызова справки или отсутствия аргументов
if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] == "--help"):
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print(f"Коэффициенты A, B, C — целые числа, по модулю не превышающие {MAX_VALUE}.")
    sys.exit(0)

# Проверка, что первая команда - это solve
if sys.argv[1] not in ("solve", "sol"):
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

# Проверка диапазона до 10000

if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    print(f"от {MAX_VALUE * -1} до {MAX_VALUE}", file=sys.stderr)
    sys.exit(1)

# Решение уравнения
if a == 0:
    if b != 0:
        print("Уравнение линейное")
        x = -c / b
        x = int(x)
        print(f"x = {x:.3f}")
        sys.exit(0)

    else:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)
else:
    print("Уравнение квадратное")
    D = b * b - 4 * a * c
    print(f"D = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
    #    if x1.is_integer():
    #         x1 = int(x1)
    #     if x2.is_integer():
    #          x2 = int(x2)

        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")
    sys.exit(0)