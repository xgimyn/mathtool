import argparse


def build_parser():
    """Создаёт и возвращает разборщик параметров командной строки."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — решение уравнений, статистика, суммы рядов и численное интегрирование",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")

    # Команда solve: решение уравнения
    p_solve = subparsers.add_parser(
        "solve",
        help="решение алгебраических уравнений вида A*x^2 + B*x + C = 0",
        allow_abbrev=False,
    )
    p_solve.add_argument("-a", type=int, help="коэффициент A")
    p_solve.add_argument("-b", type=int, help="коэффициент B")
    p_solve.add_argument("-c", type=int, help="коэффициент C")

    # Команда stats: показатели последовательности
    p_stats = subparsers.add_parser(
        "stats",
        help="вычисление показателей числовой последовательности",
        allow_abbrev=False,
    )
    p_stats.add_argument("--input", help="путь к файлу с числами")

    # Команда series: сумма ряда
    p_series = subparsers.add_parser(
        "series",
        help="вычисление суммы знакочередующегося ряда",
        allow_abbrev=False,
    )
    p_series.add_argument("--func", required=True, help="выбор ряда")
    series_group = p_series.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms", type=int, help="количество слагаемых")
    series_group.add_argument("--eps", type=float, help="точность суммирования")

    # Команда integrate: численное интегрирование
    p_integrate = subparsers.add_parser(
        "integrate",
        help="численное интегрирование функции",
        allow_abbrev=False,
    )
    p_integrate.add_argument("--func", required=True, help="выбор функции")
    p_integrate.add_argument(
        "--from",
        dest="start",
        type=float,
        required=True,
        help="нижний предел интегрирования",
    )
    p_integrate.add_argument(
        "--to",
        type=float,
        required=True,
        help="верхний предел интегрирования",
    )
    p_integrate.add_argument(
        "--steps",
        type=int,
        required=True,
        help="количество шагов разбиения",
    )

    return parser
