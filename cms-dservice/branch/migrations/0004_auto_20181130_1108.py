# Generated by Django 2.1.3 on 2018-11-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_auto_20181129_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockadjuststatement',
            name='bill_number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
