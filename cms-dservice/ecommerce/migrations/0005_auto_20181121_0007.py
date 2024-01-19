# Generated by Django 2.1.1 on 2018-11-20 17:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20181101_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropShipPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('formula', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='DropShipPromotionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('meta', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Product Class',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='dropshippromotion',
            name='items',
            field=models.ManyToManyField(blank=True, to='ecommerce.ProductClass'),
        ),
        migrations.AddField(
            model_name='dropshippromotion',
            name='types',
            field=models.ManyToManyField(blank=True, to='ecommerce.DropShipPromotionType'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.ProductClass'),
        ),
    ]