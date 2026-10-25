import sys
import cli
from calc import equation


# Обработка команды solve
def handle_solve(args):
    """Обрабатывает команду solve и возвращает код завершения."""
    if args.a is None and args.b is None and args.c is None:
        # Ввод коэффициентов с клавиатуры
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    elif args.a is not None and args.b is not None and args.c is not None:
        # Коэффициенты переданы через аргументы
        a = args.a
        b = args.b
        c = args.c
    else:
        # Задана только часть коэффициентов — ошибка в данных
        raise ValueError("укажите все три коэффициента либо ни одного")

    # Решение через модуль calc.equation
    kind, d, roots = equation.solve(a, b, c)

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

    return 0


# Обработчики для остальных команд (будут реализованы в следующих шагах)
def handle_stats(args):
    """Обработчик команды stats."""
    return 0


def handle_series(args):
    """Обработчик команды series."""
    return 0


def handle_integrate(args):
    """Обработчик команды integrate."""
    return 0


HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


# Точка входа: разбор аргументов и вызов обработчика
def main(argv):
    """Точка входа: разбирает параметры и вызывает обработчик команды."""
    parser = cli.build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
