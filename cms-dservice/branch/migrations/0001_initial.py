# Generated by Django 2.1.1 on 2018-10-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcode', models.CharField(max_length=255)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('qtys', models.IntegerField()),
                ('qtyr', models.IntegerField()),
                ('qtyd', models.IntegerField()),
                ('ud', models.CharField(max_length=255)),
                ('inv_code', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Item Stock',
                'db_table': 'ali_product_invent',
            },
        ),
        migrations.CreateModel(
            name='BranchGoodTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=255, null=True)),
                ('name_f', models.CharField(max_length=255)),
                ('client_name', models.CharField(db_column='name_t', max_length=255)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('sctime', models.DateTimeField()),
                ('to_branch', models.CharField(blank=True, db_column='inv_code', max_length=255, null=True)),
                ('lid', models.CharField(max_length=255)),
                ('from_branch', models.CharField(db_column='inv_from', max_length=255)),
                ('mcode', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('usercode', models.CharField(blank=True, max_length=3, null=True)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('trnf', models.CharField(blank=True, max_length=1, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('create_by', models.CharField(db_column='uid', max_length=255)),
                ('dl', models.CharField(max_length=1)),
                ('cancel', models.IntegerField()),
                ('send', models.IntegerField()),
                ('txtoption', models.TextField()),
                ('chkcash', models.CharField(db_column='chkCash', max_length=255)),
                ('chkfuture', models.CharField(db_column='chkFuture', max_length=255)),
                ('chktransfer', models.CharField(db_column='chkTransfer', max_length=255)),
                ('chkcredit1', models.CharField(db_column='chkCredit1', max_length=255)),
                ('chkcredit2', models.CharField(db_column='chkCredit2', max_length=255)),
                ('chkcredit3', models.CharField(db_column='chkCredit3', max_length=255)),
                ('chkinternet', models.CharField(db_column='chkInternet', max_length=255)),
                ('chkdiscount', models.CharField(db_column='chkDiscount', max_length=255)),
                ('chkother', models.CharField(db_column='chkOther', max_length=255)),
                ('txtcash', models.CharField(db_column='txtCash', max_length=255)),
                ('txtfuture', models.CharField(db_column='txtFuture', max_length=255)),
                ('txttransfer', models.CharField(db_column='txtTransfer', max_length=255)),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('txtcredit1', models.CharField(db_column='txtCredit1', max_length=255)),
                ('txtcredit2', models.CharField(db_column='txtCredit2', max_length=255)),
                ('txtcredit3', models.CharField(db_column='txtCredit3', max_length=255)),
                ('txtinternet', models.CharField(db_column='txtInternet', max_length=255)),
                ('txtdiscount', models.CharField(db_column='txtDiscount', max_length=255)),
                ('txtother', models.CharField(db_column='txtOther', max_length=255)),
                ('optioncash', models.CharField(db_column='optionCash', max_length=255)),
                ('optionfuture', models.CharField(db_column='optionFuture', max_length=255)),
                ('optiontransfer', models.CharField(db_column='optionTransfer', max_length=255)),
                ('optioncredit1', models.CharField(db_column='optionCredit1', max_length=255)),
                ('optioncredit2', models.CharField(db_column='optionCredit2', max_length=255)),
                ('optioncredit3', models.CharField(db_column='optionCredit3', max_length=255)),
                ('optioninternet', models.CharField(db_column='optionInternet', max_length=255)),
                ('optiondiscount', models.CharField(db_column='optionDiscount', max_length=255)),
                ('optionother', models.CharField(db_column='optionOther', max_length=255)),
                ('discount', models.IntegerField()),
                ('send_status', models.IntegerField(db_column='sender')),
                ('send_date', models.DateField(db_column='sender_date')),
                ('receive_status', models.IntegerField(db_column='receive')),
                ('receive_date', models.DateField()),
                ('print', models.IntegerField()),
                ('ewallet_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallett_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallett_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cancel_date', models.DateField()),
                ('uid_cancel', models.CharField(max_length=255)),
                ('mbase', models.CharField(max_length=255)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('locationbase', models.IntegerField()),
                ('crate', models.DecimalField(decimal_places=6, max_digits=11)),
                ('checkportal', models.IntegerField()),
                ('receive_by', models.CharField(db_column='uid_receive', max_length=255)),
                ('sender_by', models.CharField(db_column='uid_sender', max_length=255)),
                ('caddress', models.TextField()),
                ('cdistrictid', models.CharField(db_column='cdistrictId', max_length=255)),
                ('camphurid', models.CharField(db_column='camphurId', max_length=255)),
                ('cprovinceid', models.CharField(db_column='cprovinceId', max_length=255)),
                ('czip', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': ('ali_isaleh',),
                'ordering': ('id', 'sctime'),
            },
        ),
        migrations.CreateModel(
            name='BranchGoodTransferItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=7, null=True)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=7, null=True)),
                ('pcode', models.CharField(blank=True, max_length=20, null=True)),
                ('pdesc', models.CharField(blank=True, max_length=100, null=True)),
                ('mcode', models.CharField(blank=True, max_length=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('uidbase', models.CharField(max_length=255)),
                ('locationbase', models.IntegerField()),
                ('outstanding', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ali_isaled',
            },
        ),
        migrations.CreateModel(
            name='BranchImportStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.IntegerField(blank=True, null=True)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('inv_code_to', models.CharField(max_length=255)),
                ('mcode', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('usercode', models.CharField(blank=True, max_length=3, null=True)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('trnf', models.CharField(blank=True, max_length=1, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('uid', models.CharField(max_length=255)),
                ('dl', models.CharField(max_length=1)),
                ('cancel', models.IntegerField()),
                ('send', models.IntegerField()),
                ('txtoption', models.TextField()),
                ('chkcash', models.CharField(db_column='chkCash', max_length=255)),
                ('chkfuture', models.CharField(db_column='chkFuture', max_length=255)),
                ('chktransfer', models.CharField(db_column='chkTransfer', max_length=255)),
                ('chkcredit1', models.CharField(db_column='chkCredit1', max_length=255)),
                ('chkcredit2', models.CharField(db_column='chkCredit2', max_length=255)),
                ('chkcredit3', models.CharField(db_column='chkCredit3', max_length=255)),
                ('chkinternet', models.CharField(db_column='chkInternet', max_length=255)),
                ('chkdiscount', models.CharField(db_column='chkDiscount', max_length=255)),
                ('chkother', models.CharField(db_column='chkOther', max_length=255)),
                ('txtcash', models.CharField(db_column='txtCash', max_length=255)),
                ('txtfuture', models.CharField(db_column='txtFuture', max_length=255)),
                ('txttransfer', models.CharField(db_column='txtTransfer', max_length=255)),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('txtcredit1', models.CharField(db_column='txtCredit1', max_length=255)),
                ('txtcredit2', models.CharField(db_column='txtCredit2', max_length=255)),
                ('txtcredit3', models.CharField(db_column='txtCredit3', max_length=255)),
                ('txtinternet', models.CharField(db_column='txtInternet', max_length=255)),
                ('txtdiscount', models.CharField(db_column='txtDiscount', max_length=255)),
                ('txtother', models.CharField(db_column='txtOther', max_length=255)),
                ('optioncash', models.CharField(db_column='optionCash', max_length=255)),
                ('optionfuture', models.CharField(db_column='optionFuture', max_length=255)),
                ('optiontransfer', models.CharField(db_column='optionTransfer', max_length=255)),
                ('optioncredit1', models.CharField(db_column='optionCredit1', max_length=255)),
                ('optioncredit2', models.CharField(db_column='optionCredit2', max_length=255)),
                ('optioncredit3', models.CharField(db_column='optionCredit3', max_length=255)),
                ('optioninternet', models.CharField(db_column='optionInternet', max_length=255)),
                ('optiondiscount', models.CharField(db_column='optionDiscount', max_length=255)),
                ('optionother', models.CharField(db_column='optionOther', max_length=255)),
                ('discount', models.IntegerField()),
                ('sender', models.IntegerField()),
                ('sender_date', models.DateField()),
                ('receive', models.IntegerField()),
                ('receive_date', models.DateField()),
                ('print', models.IntegerField()),
                ('ewallet_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallett_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallett_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cancel_date', models.DateField()),
                ('uid_cancel', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ali_import_stock_h',
            },
        ),
        migrations.CreateModel(
            name='BranchImportStockItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=7, null=True)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('pcode', models.CharField(blank=True, max_length=20, null=True)),
                ('pdesc', models.CharField(blank=True, max_length=40, null=True)),
                ('mcode', models.CharField(blank=True, max_length=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('qty_old', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'ali_import_stock_d',
            },
        ),
        migrations.CreateModel(
            name='BranchTransferHq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=255, null=True)),
                ('name_f', models.CharField(max_length=255)),
                ('name_t', models.CharField(max_length=255)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('sctime', models.DateTimeField()),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('lid', models.CharField(max_length=255)),
                ('inv_from', models.CharField(max_length=255)),
                ('mcode', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tot_fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('usercode', models.CharField(blank=True, max_length=3, null=True)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('trnf', models.CharField(blank=True, max_length=1, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('uid', models.CharField(max_length=255)),
                ('dl', models.CharField(max_length=1)),
                ('cancel', models.IntegerField()),
                ('send', models.IntegerField()),
                ('txtoption', models.TextField()),
                ('chkcash', models.CharField(db_column='chkCash', max_length=255)),
                ('chkfuture', models.CharField(db_column='chkFuture', max_length=255)),
                ('chktransfer', models.CharField(db_column='chkTransfer', max_length=255)),
                ('chkcredit1', models.CharField(db_column='chkCredit1', max_length=255)),
                ('chkcredit2', models.CharField(db_column='chkCredit2', max_length=255)),
                ('chkcredit3', models.CharField(db_column='chkCredit3', max_length=255)),
                ('chkinternet', models.CharField(db_column='chkInternet', max_length=255)),
                ('chkdiscount', models.CharField(db_column='chkDiscount', max_length=255)),
                ('chkother', models.CharField(db_column='chkOther', max_length=255)),
                ('txtcash', models.CharField(db_column='txtCash', max_length=255)),
                ('txtfuture', models.CharField(db_column='txtFuture', max_length=255)),
                ('txttransfer', models.CharField(db_column='txtTransfer', max_length=255)),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('txtcredit1', models.CharField(db_column='txtCredit1', max_length=255)),
                ('txtcredit2', models.CharField(db_column='txtCredit2', max_length=255)),
                ('txtcredit3', models.CharField(db_column='txtCredit3', max_length=255)),
                ('txtinternet', models.CharField(db_column='txtInternet', max_length=255)),
                ('txtdiscount', models.CharField(db_column='txtDiscount', max_length=255)),
                ('txtother', models.CharField(db_column='txtOther', max_length=255)),
                ('optioncash', models.CharField(db_column='optionCash', max_length=255)),
                ('optionfuture', models.CharField(db_column='optionFuture', max_length=255)),
                ('optiontransfer', models.CharField(db_column='optionTransfer', max_length=255)),
                ('optioncredit1', models.CharField(db_column='optionCredit1', max_length=255)),
                ('optioncredit2', models.CharField(db_column='optionCredit2', max_length=255)),
                ('optioncredit3', models.CharField(db_column='optionCredit3', max_length=255)),
                ('optioninternet', models.CharField(db_column='optionInternet', max_length=255)),
                ('optiondiscount', models.CharField(db_column='optionDiscount', max_length=255)),
                ('optionother', models.CharField(db_column='optionOther', max_length=255)),
                ('discount', models.IntegerField()),
                ('sender', models.IntegerField()),
                ('sender_date', models.DateField()),
                ('receive', models.IntegerField()),
                ('receive_date', models.DateField()),
                ('print', models.IntegerField()),
                ('ewallet_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallett_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallett_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cancel_date', models.DateField()),
                ('uid_cancel', models.CharField(max_length=255)),
                ('mbase', models.CharField(max_length=255)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('locationbase', models.IntegerField()),
                ('crate', models.DecimalField(decimal_places=6, max_digits=11)),
                ('checkportal', models.IntegerField()),
                ('uid_receive', models.CharField(max_length=255)),
                ('uid_sender', models.CharField(max_length=255)),
                ('caddress', models.TextField()),
                ('cdistrictid', models.CharField(db_column='cdistrictId', max_length=255)),
                ('camphurid', models.CharField(db_column='camphurId', max_length=255)),
                ('cprovinceid', models.CharField(db_column='cprovinceId', max_length=255)),
                ('czip', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'ali_tsaleh',
            },
        ),
        migrations.CreateModel(
            name='BranchTransferHqItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.IntegerField()),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=7, null=True)),
                ('pcode', models.CharField(blank=True, max_length=20, null=True)),
                ('pdesc', models.CharField(blank=True, max_length=100, null=True)),
                ('mcode', models.CharField(blank=True, max_length=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('uidbase', models.CharField(max_length=255)),
                ('locationbase', models.IntegerField()),
                ('outstanding', models.CharField(max_length=255)),
                ('uidm', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ali_tsaled',
            },
        ),
    ]