# Generated by Django 2.1.3 on 2019-02-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0014_auto_20190227_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]