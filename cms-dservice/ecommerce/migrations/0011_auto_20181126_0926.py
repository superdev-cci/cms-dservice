# Generated by Django 2.1.3 on 2018-11-26 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_auto_20181126_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='product_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]