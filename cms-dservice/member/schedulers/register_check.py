from datetime import date, datetime, timedelta
from django.db.models import Q, F, Value
from django.db.models.functions import Concat

from member.models import Member
from member.models import MemberStatusStack
from member.models import MemberLogs

class RegisterCheckup():
    def get_terminate_date(self):
        expire_date = date.today() - timedelta(30)
        return expire_date

    def get_suspend_date(self):
        expire_date = date.today() - timedelta(7)
        return expire_date

    def process_check_document(self):
        last_date = self.get_suspend_date()
        queryset = Member.objects.filter(distributor_date__lte=last_date, cmp2='',
                                         status_suspend=0, status_terminate=0) \
            .filter(~Q(level__in=('MB', 'TN'), distributor_date=None))
        # Push to suspend state
        members = {x.mcode: x for x in queryset}
        logs = []
        stack_instance = []
        # Try get member status stack
        stack = MemberStatusStack.objects.filter(member__mcode__in=members.keys(), stack_type='S') \
            .select_related('member')
        if len(stack):
            for x in stack:
                members.pop(x.member.code)

        for k, v in members.items():
            stack_instance.append(MemberStatusStack(member=v, stack_type='S'))
            logs.append(MemberLogs(member=v, topic='S', change='book bank not completed (Suspend)'))

        # Create all object
        print('Suspend Effective record is : {:,}'.format(len(stack_instance)))
        if len(stack_instance):
            MemberLogs.objects.bulk_create(logs)
            MemberStatusStack.objects.bulk_create(stack_instance)
            return Member.objects.filter(mcode__in=members.keys()) \
                .update(status_suspend=1, suspend_date=datetime.today(),
                        txtoption=Concat('txtoption',
                                         Value(" Suspend with book bank ({})"
                                               .format(datetime.today().strftime('%Y-%m-%d'))))
                        )
        return 0

    def process_terminate(self):
        last_date = self.get_terminate_date()
        queryset = Member.objects.filter(distributor_date__lte=last_date, cmp2='', status_terminate=0) \
            .filter(~Q(level__in=('MB', 'TN',), distributor_date=None))
        # queryset = MemberStatusStack.objects.filter(issue_date__lte=last_date, stack_type='S').select_related('member')
        # Receive data from database
        logs = []
        for item in queryset:
            logs.append(MemberLogs(member=item, topic='T', change='book bank not completed (Terminate)'))

        print('Terminate Effective record is : {:,}'.format(len(logs)))
        if len(logs):
            MemberLogs.objects.bulk_create(logs)
            return queryset.update(
                status_terminate=1,
                terminate_date=datetime.today(),
                txtoption=Concat('txtoption',
                                 Value(" Terminate with bookbank ({})".format(datetime.today().strftime('%Y-%m-%d'))))
            )
        return 0

    def revoke_status(self, member):
        queryset = MemberStatusStack.objects.filter(member=member, stack_type='S').select_related('member')
        if len(queryset):
            queryset.delete()
            MemberLogs.objects.create(members=member, topic='S', change='Revoke status (Suspend)')
            return True
        return False
