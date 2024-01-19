import calendar
import datetime
from dateutil import relativedelta


class MonthMixIn(object):
    """
    a non-attribute class base contain a date operation method
    """
    def _calculate_period(self, date):
        """
        a method use to find start date and end date of month from input date

        :param date: (:obj:`date`) The date representing the month

        :return: start date and end date of month
        """
        month = calendar.monthrange(date.year, date.month)
        last_date = month[1]
        start = date.replace(day=1)
        end = date.replace(day=last_date)
        return start, end

    def _calculate_month_range(self, start, end):
        """
        a method use to find a list of month from start date and end date

        :param start: (:obj:`date`) The date representing the start month

        :param end: (:obj:`date`) The date representing the end month

        :return: list of month from start month to end month or None in case start month greater than end month
        """
        month_range = []
        start_month = start.month
        end_month = end.month

        if start_month > end_month:
            return None

        diff = (end_month - start_month) + 1

        for i in range(diff):
            month_range.append(start.replace(month=start_month + i))
        return month_range

    def _calculate_year_range(self, start, end):
        """
        a method use to find a list of year from start date and end date

        :param start: (:obj:`date`) The date representing the start year

        :param end: (:obj:`date`) The date representing the end year

        :return: list of year from start year to end year or None in case start year greater than end year
        """
        year_range = []
        start_year = start.year

        end_year = end.year

        if start_year > end_year:
            return None

        diff = (end_year - start_year) + 1

        for i in range(diff):
            year_range.append(start.replace(year=start_year + i, ))
        return year_range

    def next_day(self, current_date):
        """
        a method use to find a next date from current date

        :param current_date: (:obj:`date`) an input date

        :return: tomorrow of input date
        """
        try:
            next_date = current_date.replace(day=current_date.day + 1)
        except:
            return self.next_month(current_date)
        return next_date

    def next_month(self, current_month):
        """
        a method use to find a next month from current month

        :param current_month: (:obj:`date`) an input month

        :return: (:obj:`date`) next month of input month
        """
        try:
            next_date = current_month.replace(day=1, month=current_month.month + 1)
        except:
            next_date = current_month.replace(year=current_month.year + 1, month=1, day=1)
        return next_date

    def get_next_key(self, current_date):
        """
        a method use to find a next key(date) for access data in dictionary

        :param current_date: (:obj:`date`) current key(date)

        :return: (:obj:`date`) next key(date) of input key
        """
        if self.get_type == 'daily':
            next_date = self.next_day(current_date)
        else:
            next_date = self.next_month(current_date)
        return next_date

    @staticmethod
    def get_month_range(date):
        """
        a method use to find start date and end date of month from input date

        :param date: (:obj:`date`) or (str) The date representing the month

        :return: start date (:obj:`date`) and end date (:obj:`date`) of month
        """
        if isinstance(date, str):
            start = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            start = date
        month = calendar.monthrange(start.year, start.month)
        last_date = month[1]
        start_date = start.replace(day=1)
        end_date = start.replace(day=last_date)
        return start_date, end_date

    @staticmethod
    def get_year_range(date):
        """
        a method use to find start date and end date of year from input date

        :param date: (:obj:`date`) or (str) The date representing the year

        :return: start date (:obj:`date`) and end date (:obj:`date`) of year
        """
        if isinstance(date, str):
            start = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            start = date
        start_date = start.replace(day=1, month=1)
        end_date = start.replace(day=31, month=12)
        return start_date, end_date

    @staticmethod
    def month_diff_range(end, start):
        """
        a method use to find a list of month from start date and end date

        :param start: (:obj:`date`) The date representing the start month

        :param end: (:obj:`date`) The date representing the end month

        :return: list of month from start month to end month
        """
        route = []
        diff = relativedelta.relativedelta(end, start)
        current = start.replace(day=1)
        for i in range(0, ((diff.years * 12) + diff.months + 1)):
            route.append(current)
            month = current.month
            month += 1
            if month > 12:
                current = current.replace(month=1, year=current.year + 1)
            else:
                current = current.replace(month=month)
        return route

    @staticmethod
    def get_week_range(date):
        """
        a method use to find start date and end date of week from input date

        :param date: (:obj:`date`) or (str) The date representing the week

        :return: start date (:obj:`date`) and end date (:obj:`date`) of week
        """
        if isinstance(date, str):
            input_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            input_date = date
        if 1 <= input_date.day < 8:
            start_date = input_date.replace(day=1)
            end_date = input_date.replace(day=7)
        elif 8 <= input_date.day < 15:
            start_date = input_date.replace(day=8)
            end_date = input_date.replace(day=14)
        elif 15 <= input_date.day < 22:
            start_date = input_date.replace(day=15)
            end_date = input_date.replace(day=21)
        else: #22 <= input_date.day
            start_date = input_date.replace(day=22)
            end_date = input_date.replace(day=calendar.monthrange(input_date.year, input_date.month)[1])
        return start_date, end_date