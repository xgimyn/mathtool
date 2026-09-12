import math
import sys

# Проверка вызова справки или отсутствия аргументов
if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] == "--help"):
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print("Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")
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

# Проверка диапазона до 10000
MAX_VALUE = 10000
if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)

# Решение уравнения
if a == 0:
    if b != 0:
        print("Уравнение линейное")
        x = -c / b
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
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")
    sys.exit(0)