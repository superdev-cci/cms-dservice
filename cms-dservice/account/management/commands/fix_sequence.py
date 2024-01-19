import sys

from django.contrib.auth.management import _get_all_permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.apps import apps
from django.core.management import call_command
from django.conf import settings
from django.db import connection
from django.core.management import call_command
from django.db import connection
from django.apps import apps
from io import StringIO


class Command(BaseCommand):
    help = "Fix sequence for proxy models."

    def handle(self, *args, **options):
        commands = StringIO()
        cursor = connection.cursor()

        for app in apps.get_app_configs():
            call_command('sqlsequencereset', app.label, stdout=commands)

        print(commands.getvalue())
        return
