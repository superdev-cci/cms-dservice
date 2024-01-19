import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from account.models import UserAccount
from members.models import Member


class Command(BaseCommand):
    help = "Create user account"

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='username')
        parser.add_argument('--password', type=str, help='password')
        parser.add_argument('--member', type=str, help='member_code')

    def handle(self, *args, **options):
        username = options.get('username', '')
        password = options.get('password', '')
        member = options.get('member', '')

        if member != '':
            try:
                member = Member.objects.get(member_code=member)
            except:
                member = None
                pass

        if member is not None:
            user = User(username=member.code)
            user.set_password(password)
            user.save()
            user_acc = UserAccount(user=user, member=member)
        else:
            user = User(username=username, password=password)
            user.set_password(password)
            user.save()
            user_acc = UserAccount(user=user)

        user_acc.save()
        print('Create successful!!!')

        return
