import math
import argparse
import sys


count_none = 0


def is_correct_value(value):
    global count_none
    if value is None:
        count_none += 1
        return True
    else:
        try:
            value = float(value)
            return value > 0 or value is None
        except ValueError:
            return False


parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=["annuity", "diff"])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

if len(sys.argv) == 5 and is_correct_value(args.payment) and is_correct_value(args.principal) \
        and is_correct_value(args.periods) and is_correct_value(args.interest) and count_none == 1:

    payment = float(args.payment) if args.payment is not None else args.payment
    principal = int(args.principal) if args.principal is not None else args.principal
    periods = int(args.periods) if args.periods is not None else args.periods
    interest = float(args.interest) if args.interest is not None else args.interest

    i = interest / (12 * 100)

    if payment is None:
        if args.type == "annuity":
            m = math.ceil(principal * i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
            print(f'Your monthly payment = {m}!')
        elif args.type == "diff":
            all_pay = 0
            for p in range(0, periods):
                diff_m = math.ceil(principal / periods + i * (principal - principal * p / periods))
                all_pay += diff_m
                print(f'Month {p + 1}: payment is {diff_m}')
            print(f'Overpayment = {principal - all_pay}')

    elif principal is None:
        p = math.ceil(payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
        print(f'Your loan principal = {p}!')
        print(f'Overpayment = {payment * periods - p}')

    elif periods is None:
        n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
        month = f'and {n % 12} months' if n % 12 > 0 else ''
        print(f'It will take {n // 12} years {month} to repay this loan!')
        print(f'Overpayment = {payment * n - principal}')

else:
    print('Incorrect parameters')
