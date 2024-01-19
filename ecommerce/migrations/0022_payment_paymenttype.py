# Generated by Django 2.1.3 on 2019-01-30 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_saleinvoice_credit_note_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=64)),
                ('code', models.CharField(default=' ', max_length=4)),
                ('payment_type', models.CharField(blank=True, choices=[('CA', 'CASH'), ('TR', 'TRANSFER'), ('CE', 'Credit'), ('TP', 'P2P'), ('VC', 'VOUCHER')], max_length=4, null=True)),
                ('amount', models.FloatField(default=0)),
                ('remark', models.CharField(blank=True, max_length=64, null=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.SaleInvoice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=64)),
                ('code', models.CharField(default=' ', max_length=4)),
                ('enable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
