# Generated by Django 2.1.3 on 2019-01-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='balance_discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_type',
            field=models.CharField(blank=True, choices=[('IN', 'InBound'), ('OS', 'Oversea')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='tripapplication',
            name='confirm_count',
            field=models.IntegerField(default=0),
        ),
    ]
