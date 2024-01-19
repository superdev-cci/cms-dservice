import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = "Update suspend / terminate user account"

    def handle(self, *args, **options):

        user = User.objects.select_related('useraccount__member', 'useraccount')\
            .filter(useraccount__member__status__code__in=['TR', 'SP'])

        user.update(is_active=False)

        print('Update to de-active : {}'.count(user.count()))
        return
