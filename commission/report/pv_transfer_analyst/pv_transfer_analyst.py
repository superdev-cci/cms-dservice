from django.db.models import Count, Max, Min, Avg, Q, Sum

from commission.models import PvTransfer
from core.report.summary import PeriodSummaryBase
from member.models import Member


class SummaryPvTransferAgencyAnalyst(PeriodSummaryBase):
    """
    a class represent agency member's PV transfer activity
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(SummaryPvTransferAgencyAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.agency_list = Member.objects.filter(Q(mtype1=2), ~Q(mcode='TH0123456')).values_list("mcode", flat=True)

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        return queryset.filter(uid__in=self.agency_list)

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        primary_instance = self.get_query_set(self.start, self.end, self.get_type)
        for mcode in self.agency_list:
            pool[mcode] = {}
            instance_a = primary_instance.filter(uid=mcode, sa_type__in=["A", "AM"]).values("time", "sa_type").annotate(
                count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")
            ).order_by("time", "count")
            if instance_a:
                pool[mcode]["a/am"] = instance_a
            instance_y200 = primary_instance.filter(uid=mcode, sa_type="Y", tot_pv=200).values("time",
                                                                                               "sa_type").annotate(
                count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")
            ).order_by("time", "count")
            if instance_y200:
                pool[mcode]["y200"] = instance_y200
            instance_yf = primary_instance.filter(Q(uid=mcode), Q(sa_type="Y"), ~Q(tot_pv=200),
                                                  Q(member__mtype1=1)).values("time", "sa_type").annotate(
                count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")
            ).order_by("time", "count")
            if instance_yf:
                pool[mcode]["yf"] = instance_yf
            instance_ym = primary_instance.filter(Q(uid=mcode), Q(sa_type="Y"), ~Q(tot_pv=200),
                                                  ~Q(member__mtype1=1)).values("time", "sa_type").annotate(
                count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")
            ).order_by("time", "count")
            if instance_ym:
                pool[mcode]["ym"] = instance_ym
        return pool


class SummaryPvTransferReceiverAnalyst(PeriodSummaryBase):
    """
    a class represent agency member's PV transfer activity with their sponsor tree
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(SummaryPvTransferReceiverAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.agency_list = Member.objects.filter(Q(mtype1=2), ~Q(mcode='TH0123456')).values_list("mcode", flat=True)

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        return queryset.filter(uid__in=self.agency_list)

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        primary_instance = self.get_query_set(self.start, self.end, self.get_type)
        instance_y200 = primary_instance.filter(sa_type="Y", tot_pv=200).values(
            "time", "mcode", "name_t", "sa_type").annotate(
            count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")).order_by(
            "mcode", "time", "count")
        for i in instance_y200:
            if i["mcode"] not in pool:
                pool[i["mcode"]] = {"y200": [], "a/am": [], "yf": [], "ym": []}
                pool[i["mcode"]]["y200"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
            else:
                pool[i["mcode"]]["y200"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
        instance_ym = primary_instance.filter(~Q(member__mtype1=1), Q(sa_type="Y"), ~Q(tot_pv=200)).values(
            "time", "mcode", "name_t", "sa_type").annotate(
            count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")).order_by(
            "mcode", "time", "count")
        for i in instance_ym:
            if i["mcode"] not in pool:
                pool[i["mcode"]] = {"y200": [], "a/am": [], "yf": [], "ym": []}
                pool[i["mcode"]]["ym"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
            else:
                pool[i["mcode"]]["ym"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
        instance_yf = primary_instance.filter(Q(member__mtype1=1), Q(sa_type="Y"), ~Q(tot_pv=200)).values(
            "time", "mcode", "name_t", "sa_type").annotate(
            count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")).order_by(
            "mcode", "time", "count")
        for i in instance_yf:
            if i["mcode"] not in pool:
                pool[i["mcode"]] = {"y200": [], "a/am": [], "yf": [], "ym": []}
                pool[i["mcode"]]["yf"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
            else:
                pool[i["mcode"]]["yf"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
        instance_a = primary_instance.filter(sa_type__in=["A", "AM"]).values(
            "time", "mcode", "name_t", "sa_type").annotate(
            count=Count("id"), min=Min("tot_pv"), avg=Avg("tot_pv"), max=Max("tot_pv"), sum_pv=Sum("tot_pv")).order_by(
            "mcode", "time", "count")
        for i in instance_a:
            if i["mcode"] not in pool:
                pool[i["mcode"]] = {"y200": [], "a/am": [], "yf": [], "ym": []}
                pool[i["mcode"]]["a/am"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
            else:
                pool[i["mcode"]]["a/am"].append(i)
                # pool[i["mcode"]]["total"] += i["count"]
        return pool


class SummaryPvTransferAnalyst(PeriodSummaryBase):
    """
    a class represent agency member's PV transfer activity Focus Franchise
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(SummaryPvTransferAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.agency_list = Member.objects.filter(Q(mtype1=2), ~Q(mcode='TH0123456')).values_list("mcode", flat=True)

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        return queryset.filter(uid__in=self.agency_list)

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {"y200": {}, "yf": {}, "ym": {}, "a/am": {}}
        primary_instance = self.get_query_set(self.start, self.end, self.get_type)
        for mc in self.agency_list:
            # instance bill A
            instance_a = primary_instance.filter(uid=mc, sa_type__in=["A", "AM"]).values(
                "time", "mcode", "member__name_t", "sa_type").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("mcode", "time", "count")
            if instance_a:
                pool["a/am"][mc] = instance_a
            # instance bill Y 200 PV
            instance_y200 = primary_instance.filter(uid=mc, sa_type="Y", tot_pv=200).values(
                "time", "mcode", "member__name_t", "sa_type").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("mcode", "time", "count")
            if instance_y200:
                pool["y200"][mc] = instance_y200
            # instance bill Y to FR
            instance_yf = primary_instance.filter(
                Q(member__mtype1=1), Q(uid=mc), Q(sa_type="Y"), ~Q(tot_pv=200)
            ).values("time", "mcode", "member__name_t", "sa_type").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("mcode", "time", "count")
            if instance_yf:
                pool["yf"][mc] = instance_yf
            # instance bill Y Normal
            instance_ym = primary_instance.filter(
                ~Q(member__mtype1=1), Q(uid=mc), Q(sa_type="Y"), ~Q(tot_pv=200)
            ).values("time", "mcode", "member__name_t", "sa_type").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("mcode", "time", "count")
            if instance_ym:
                pool["ym"][mc] = instance_ym
        return pool


class PvTransferInnerOuterAnalyst(PeriodSummaryBase):
    """
    a class represent agency member's PV transfer activity with their downline tree.
    focus transfer in downline tree or out downline tree
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(PvTransferInnerOuterAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.agency_list = Member.objects.filter(Q(mtype1=2), ~Q(mcode='TH0123456'))

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        return queryset.filter(uid__in=self.agency_list.values_list('mcode', flat=True))

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        primary_instance = self.get_query_set(self.start, self.end, self.get_type)
        for agency in self.agency_list:
            pool[agency.mcode] = {
                "name": agency.full_name,
                "y200": {"all_bill": [], "inner_bill": [], "outer_bill": []},
                "y": {"all_bill": [], "inner_bill": [], "outer_bill": []},
                "a/am": {"all_bill": [], "inner_bill": [], "outer_bill": []}
            }
            all_a = primary_instance.filter(
                uid=agency.mcode,
                sa_type__in=["A", "AM"]
            ).values("mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if all_a:
                pool[agency.mcode]["a/am"]["all_bill"] = all_a
            inner_a = primary_instance.filter(
                uid=agency.mcode,
                sa_type__in=["A", "AM"],
                member__line_lft__gt=agency.line_lft,
                member__line_rgt__lt=agency.line_rgt,
            ).values("mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if inner_a:
                pool[agency.mcode]["a/am"]["inner_bill"] = inner_a
            outer_a = primary_instance.filter(
                uid=agency.mcode,
                sa_type__in=["A", "AM"],
            ).filter(~Q(member__line_lft__gt=agency.line_lft, member__line_rgt__lt=agency.line_rgt)).values(
                "mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if outer_a:
                pool[agency.mcode]["a/am"]["outer_bill"] = outer_a
            # End A instance Start Y instance
            # ----- group Y only 200 PV -----
            primary_y = primary_instance.filter(
                Q(uid=agency.mcode),
                Q(sa_type="Y")
            )
            receiver_list = primary_y.values_list('mcode', flat=True).distinct()
            y200_list = []
            y_list = []
            for mc in receiver_list:
                pv_list = primary_y.filter(mcode=mc).values_list('tot_pv', flat=True)
                if all(elem == 200 for elem in pv_list):
                    y200_list.append(mc)
                else:
                    y_list.append(mc)
            # all_y = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     ~Q(tot_pv=200)
            all_y = primary_y.filter(
                mcode__in=y_list
            ).values("mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if all_y:
                pool[agency.mcode]["y"]["all_bill"] = all_y
            # inner_y = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     ~Q(tot_pv=200),
            inner_y = primary_y.filter(
                Q(mcode__in=y_list),
                Q(member__line_lft__gt=agency.line_lft),
                Q(member__line_rgt__lt=agency.line_rgt),
            ).values("mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if inner_y:
                pool[agency.mcode]["y"]["inner_bill"] = inner_y
            # outer_y = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     ~Q(tot_pv=200),
            outer_y = primary_y.filter(
                mcode__in=y_list
            ).filter(~Q(member__line_lft__gt=agency.line_lft, member__line_rgt__lt=agency.line_rgt)).values(
                "mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if outer_y:
                pool[agency.mcode]["y"]["outer_bill"] = outer_y
            # # End Y instance Start Y200 instance
            # all_y200 = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     Q(tot_pv=200)
            all_y200 = primary_y.filter(
                mcode__in=y200_list
            ).values("mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if all_y200:
                pool[agency.mcode]["y200"]["all_bill"] = all_y200
            # inner_y200 = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     Q(tot_pv=200),
            inner_y200 = primary_y.filter(
                Q(mcode__in=y200_list),
                Q(member__line_lft__gt=agency.line_lft),
                Q(member__line_rgt__lt=agency.line_rgt),
            ).values("mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if inner_y200:
                pool[agency.mcode]["y200"]["inner_bill"] = inner_y200
            # outer_y200 = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     Q(tot_pv=200),
            outer_y200 = primary_y.filter(
                mcode__in=y200_list
            ).filter(~Q(member__line_lft__gt=agency.line_lft, member__line_rgt__lt=agency.line_rgt)).values(
                "mcode").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if outer_y200:
                pool[agency.mcode]["y200"]["outer_bill"] = outer_y200
        return pool


class SummaryPvTransferInOutAnalyst(PeriodSummaryBase):
    """
    a class represent agency member's summary PV transfer activity with their downline tree
    focus transfer in downline tree or out downline tree
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(SummaryPvTransferInOutAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.agency_list = Member.objects.filter(Q(mtype1=2), ~Q(mcode='TH0123456'))

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        return queryset.filter(uid__in=self.agency_list.values_list('mcode', flat=True))

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        primary_instance = self.get_query_set(self.start, self.end, self.get_type)
        for agency in self.agency_list:
            pool[agency.mcode] = {
                "name": agency.full_name,
                "y200": {"all_bill": [], "inner_bill": [], "outer_bill": []},
                "y": {"all_bill": [], "inner_bill": [], "outer_bill": []},
                "a/am": {"all_bill": [], "inner_bill": [], "outer_bill": []}
            }
            all_a = primary_instance.filter(
                uid=agency.mcode,
                sa_type__in=["A", "AM"]
            ).values("uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if all_a:
                pool[agency.mcode]["a/am"]["all_bill"] = all_a
            inner_a = primary_instance.filter(
                uid=agency.mcode,
                sa_type__in=["A", "AM"],
                member__line_lft__gt=agency.line_lft,
                member__line_rgt__lt=agency.line_rgt,
            ).values("uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if inner_a:
                pool[agency.mcode]["a/am"]["inner_bill"] = inner_a
            outer_a = primary_instance.filter(
                uid=agency.mcode,
                sa_type__in=["A", "AM"],
            ).filter(~Q(member__line_lft__gt=agency.line_lft, member__line_rgt__lt=agency.line_rgt)).values(
                "uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if outer_a:
                pool[agency.mcode]["a/am"]["outer_bill"] = outer_a
            # End A instance Start Y instance
            # ----- group Y only 200 PV -----
            primary_y = primary_instance.filter(
                Q(uid=agency.mcode),
                Q(sa_type="Y")
            )
            receiver_list = primary_y.values_list('mcode', flat=True).distinct()
            y200_list = []
            y_list = []
            for mc in receiver_list:
                pv_list = primary_y.filter(mcode=mc).values_list('tot_pv', flat=True)
                if all(elem == 200 for elem in pv_list):
                    y200_list.append(mc)
                else:
                    y_list.append(mc)
            # all_y = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     ~Q(tot_pv=200)
            all_y = primary_y.filter(
                mcode__in=y_list
            ).values("uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if all_y:
                pool[agency.mcode]["y"]["all_bill"] = all_y
            # inner_y = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     ~Q(tot_pv=200),
            inner_y = primary_y.filter(
                Q(mcode__in=y_list),
                Q(member__line_lft__gt=agency.line_lft),
                Q(member__line_rgt__lt=agency.line_rgt),
            ).values("uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if inner_y:
                pool[agency.mcode]["y"]["inner_bill"] = inner_y
            # outer_y = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     ~Q(tot_pv=200),
            outer_y = primary_y.filter(
                mcode__in=y_list
            ).filter(~Q(member__line_lft__gt=agency.line_lft, member__line_rgt__lt=agency.line_rgt)).values(
                "uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if outer_y:
                pool[agency.mcode]["y"]["outer_bill"] = outer_y
            # # End Y instance Start Y200 instance
            # all_y200 = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     Q(tot_pv=200)
            all_y200 = primary_y.filter(
                mcode__in=y200_list
            ).values("uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if all_y200:
                pool[agency.mcode]["y200"]["all_bill"] = all_y200
            # inner_y200 = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     Q(tot_pv=200),
            inner_y200 = primary_y.filter(
                Q(mcode__in=y200_list),
                Q(member__line_lft__gt=agency.line_lft),
                Q(member__line_rgt__lt=agency.line_rgt),
            ).values("uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if inner_y200:
                pool[agency.mcode]["y200"]["inner_bill"] = inner_y200
            # outer_y200 = primary_instance.filter(
            #     Q(uid=agency.mcode),
            #     Q(sa_type="Y"),
            #     Q(tot_pv=200),
            outer_y200 = primary_y.filter(
                mcode__in=y200_list
            ).filter(~Q(member__line_lft__gt=agency.line_lft, member__line_rgt__lt=agency.line_rgt)).values(
                "uid").annotate(
                count=Count("id"),
                min=Min("tot_pv"),
                avg=Avg("tot_pv"),
                max=Max("tot_pv"),
                sum_pv=Sum("tot_pv")
            ).order_by("count")
            if outer_y200:
                pool[agency.mcode]["y200"]["outer_bill"] = outer_y200
        return pool
