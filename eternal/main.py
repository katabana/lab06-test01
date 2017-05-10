import sys
import argparse


def calculate(year, month, day):
    """
    Calculates day of the week (0-Monday, 1-Tuesday)
    :param year:
    :param month:
    :param day:
    :return:
    using Disparate Gauss's algorithm variation
    """
    y = year % 100
    c = year // 100
    m = (month - 3) % 12 + 1
    day_of_the_week = int((day + (2.6 * m - 0.2) // 1 + y + (y / 4) // 1 + (c / 4) // 1 - 2 * c) % 7) - 1
    if day_of_the_week < 0:
        day_of_the_week = day_of_the_week + 7
    return day_of_the_week


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--year',
                        type=int,
                        required=True,
                        help='Year')
    parser.add_argument('--month',
                        type=int,
                        required=True,
                        help='Month')
    parser.add_argument('--day',
                        type=int,
                        required=True,
                        help='Day')
    parsed_args = parser.parse_args(args)
    weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
    print("Weekday {}".format(weekday))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
