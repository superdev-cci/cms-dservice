from commission.functions.one_time_bonus import OneTimeBonusCalculator
from datetime import datetime


def main():
    start = datetime.strptime('2019-01-01', '%Y-%m-%d').date()
    end = datetime.strptime('2019-01-31', '%Y-%m-%d').date()

    calculator = OneTimeBonusCalculator(start, end)
    calculator.calculate()
    calculator.create_report()
