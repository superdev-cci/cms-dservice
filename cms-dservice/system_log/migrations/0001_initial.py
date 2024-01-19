# Generated by Django 2.1.1 on 2018-10-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sys_id', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('object', models.TextField(blank=True, null=True)),
                ('detail', models.TextField()),
                ('chk_mobile', models.IntegerField()),
                ('chk_id_card', models.IntegerField()),
                ('chk_sp_code', models.IntegerField()),
                ('chk_upa_code', models.IntegerField()),
                ('chk_acc_no', models.IntegerField()),
                ('ip', models.CharField(blank=True, max_length=20, null=True)),
                ('logdate', models.DateField(blank=True, null=True)),
                ('logtime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'System log',
                'db_table': 'ali_log',
            },
        ),
        migrations.CreateModel(
            name='LogEautoship',
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
                ('recal', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'E-autoship log',
                'db_table': 'ali_log_eatoship',
            },
        ),
        migrations.CreateModel(
            name='LogEwallet',
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
                'verbose_name_plural': 'Ewallet log',
                'db_table': 'ali_log_ewallet',
            },
        ),
        migrations.CreateModel(
            name='LogHpv',
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
                'verbose_name_plural': 'Hpv log',
                'db_table': 'ali_log_hpv',
            },
        ),
        migrations.CreateModel(
            name='LogVoucher',
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
                'verbose_name_plural': 'Voucher log',
                'db_table': 'ali_log_voucher',
            },
        ),
        migrations.CreateModel(
            name='LogWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rcode', models.IntegerField()),
                ('fdate', models.DateField()),
                ('tdate', models.DateField()),
                ('mcode', models.CharField(max_length=255)),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('evoucher', models.DecimalField(decimal_places=2, max_digits=15)),
                ('eautoship', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ecom', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'verbose_name_plural': 'Wallet log',
                'db_table': 'ali_log_wallet',
            },
        ),
    ]