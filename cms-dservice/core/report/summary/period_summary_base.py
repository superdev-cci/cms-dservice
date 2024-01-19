from functools import reduce
import datetime
from core.mixin import MonthMixIn
import operator
from django.db import models
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter, TruncWeek


class PeriodSummaryBase(MonthMixIn):
    """
    This's a class base to get some data from Models with DatetimeField or DateField in django project.
    That's can group by 'Time-Period' [daily, monthly, quarter, yearly].
    This class inherit class `MonthMixIn` also you can use a method in MonthMixIn or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]

    Meta:
        * model (:class:`django models`): a models that's you interested to get data
        * date_fields (str): name of DatetimeField or DateField of model
        * filter (:obj:`dict`, optional): dictionary that contain key[field of model] and value[data of that field]
        * exclude (:obj:`dict`, optional): dictionary that contain key[field of model] and value[data of that field]

    Example:
        class SummaryData(PeriodSummaryBase):
            class Meta:
                model = SomeModels
                date_fields = "date_create"
                filter = {"att1": 0, "att2__gt": 10, "att3__in": ["a", "b", "c"]}
                exclude = {"att1": 1}
    """
    GET_TYPE = {
        'daily': TruncDay,
        'monthly': TruncMonth,
        'quarter': TruncQuarter,
        'yearly': TruncYear,
        'week': TruncWeek
    }

    def __init__(self, *args, **kwargs):
        self.context = kwargs
        self.start = kwargs.get('start', None)
        if isinstance(self.start, str):
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%d').date()
        elif self.start is None:
            self.start = datetime.date.today()

        self.end = kwargs.get('end', None)
        if isinstance(self.end, str):
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%d').date()
        elif self.end is None:
            self.end = datetime.date.today()

    def get_model(self):
        """
        a function to get models from meta class

        :return: django models
        """
        meta = getattr(self, 'Meta')
        return meta.model

    @property
    def date_range(self):
        """
        a property that's return a timedelta object

        :return: timedelta object
        """
        return self.end - self.start

    @property
    def period(self):
        """
        a property that's return two date object

        :return: start(:obj:`date`), end(:obj:`date`)
        """
        return self.start, self.end

    def filter_queryset(self, queryset):
        """
        a method that 'filter' a queryset with class meta.filter (with Q filter) and meta.exclude (with ~Q filter)

        :param queryset: queryset is a data set that get from model

        :return: queryset after filter
        """
        meta = self.Meta
        queries = []
        if hasattr(meta, 'filter'):
            for k, v in meta.filter.items():
                queries.append(models.Q(**{k: v}))
            queryset = queryset.filter(reduce(operator.and_, queries))

        if hasattr(meta, 'exclude'):
            queries = []
            for k, v in meta.exclude.items():
                queries.append(~models.Q(**{k: v}))
            queryset = queryset.filter(reduce(operator.and_, queries))

        return queryset

    def get_extend_queryset(self, queryset):
        """
        a method for overwrite on inherit class for manage data structure

        :param queryset: queryset is a data set that get from model

        :return: queryset after reform
        """
        return queryset

    def get_query_set(self, start=None, end=None, get_type='daily'):
        """
        main function process data from 'Model' with conditions that's identify in meta class

        :param start: date object, the start date for which we are interested in information

        :param end: date object, the end date for which we are interested in information

        :param get_type: default is 'daily' time period to group data (Optional)

        :return: queryset after process
        """
        if start is None:
            start = self.start
        if end is None:
            end = self.end
        model = self.get_model()
        meta = getattr(self, 'Meta')
        date_filter = {'{}__range'.format(meta.date_fields): (start, end)}
        query_set = model.objects.filter(**date_filter)
        query_set = self.filter_queryset(query_set)
        TruncClass = self.GET_TYPE.get(get_type, None)

        if TruncClass is None:
            raise AttributeError('wrong get_type')

        query_set = query_set.annotate(time=TruncClass(meta.date_fields))

        return self.get_extend_queryset(query_set)
