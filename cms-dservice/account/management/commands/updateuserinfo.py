import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from account.models import UserAccount
from members.models import Member


class Command(BaseCommand):
    help = "Create user account"

    def add_arguments(self, parser):
        parser.add_argument('--password', type=str, help='password')
        parser.add_argument('--member', type=str, help='member_code')

    def handle(self, *args, username='', password='', member='', **options):
        username = username
        pwd = password
        member_code = member

        if member_code != '':
            try:
                user = User.objects.select_related(
                    'useraccount__member', 'useraccount').get(username=member_code)
                member = user.useraccount.member
                user.first_name = member.person.name
                user.last_name = member.person.surname
                user.save()

                if pwd != '':
                    user.set_password(pwd)
                    user.save()
                print('{} Update successful!!!'.format(member_code))
            except:

                print('{} Update fail!!!'.format(member_code))

        return
