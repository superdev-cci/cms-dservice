# Generated by Django 2.1.3 on 2020-09-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_log', '0005_positionchangelog_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogTravelCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcode', models.CharField(max_length=255)),
                ('inv_code', models.CharField(max_length=255)),
                ('sadate', models.DateField()),
                ('satime', models.TimeField()),
                ('sano', models.CharField(max_length=255)),
                ('value_in', models.DecimalField(db_column='_in', decimal_places=2, max_digits=15)),
                ('value_out', models.DecimalField(db_column='_out', decimal_places=2, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('uid', models.CharField(max_length=255)),
                ('sa_type', models.CharField(max_length=255)),
                ('value_option', models.CharField(db_column='_option', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'TravelCredit log',
            },
        ),
    ]