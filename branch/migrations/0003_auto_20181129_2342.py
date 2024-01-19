# Generated by Django 2.1.3 on 2018-11-29 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_auto_20181129_2337'),
        ('branch', '0002_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockAdjustItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StockAdjustStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.IntegerField(blank=True, null=True)),
                ('sadate', models.DateField(default=datetime.date.today)),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('usercode', models.CharField(blank=True, max_length=3, null=True)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('cancel', models.IntegerField(blank=True, null=True)),
                ('cancel_date', models.DateField(blank=True, null=True)),
                ('uid_cancel', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-sadate', 'bill_number'),
            },
        ),
        migrations.AddField(
            model_name='stockadjustitem',
            name='bill_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.StockAdjustStatement'),
        ),
        migrations.AddField(
            model_name='stockadjustitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Product'),
        ),
    ]
