# Generated by Django 2.1.1 on 2018-10-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('pcode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sa_type', models.CharField(max_length=2)),
                ('pdesc', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('customer_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('pv', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('special_pv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bv', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('st', models.IntegerField()),
                ('sst', models.IntegerField()),
                ('bf', models.IntegerField()),
                ('ato', models.IntegerField()),
                ('ud', models.CharField(max_length=1)),
                ('locationbase', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('fdate', models.DateField()),
                ('tdate', models.DateField()),
                ('pos_mb', models.IntegerField()),
                ('pos_su', models.IntegerField()),
                ('pos_ex', models.IntegerField()),
                ('pos_br', models.IntegerField()),
                ('pos_si', models.IntegerField()),
                ('pos_go', models.IntegerField()),
                ('pos_pl', models.IntegerField()),
                ('pos_pe', models.IntegerField()),
                ('pos_ru', models.IntegerField()),
                ('pos_sa', models.IntegerField()),
                ('pos_em', models.IntegerField()),
                ('pos_di', models.IntegerField()),
                ('pos_bd', models.IntegerField()),
                ('pos_bl', models.IntegerField()),
                ('pos_cd', models.IntegerField()),
                ('pos_id', models.IntegerField()),
                ('pos_pd', models.IntegerField()),
                ('pos_rd', models.IntegerField()),
                ('vat', models.IntegerField()),
            ],
            options={
                'db_table': 'ali_product_package',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PromotionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=20)),
                ('pcode', models.CharField(max_length=20)),
                ('pdesc', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('mdate', models.DateField()),
            ],
            options={
                'db_table': 'ali_product_package1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pcode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('pdesc', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('personel_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('customer_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('pv', models.IntegerField(blank=True, null=True)),
                ('bv', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('ud', models.CharField(max_length=1, blank=True)),
                ('sync', models.CharField(blank=True, max_length=1, null=True)),
                ('web', models.CharField(blank=True, max_length=1, null=True)),
                ('st', models.IntegerField(blank=True, null=True)),
                ('sst', models.IntegerField()),
                ('bf', models.IntegerField()),
                ('sh', models.CharField(blank=True, max_length=1, null=True)),
                ('pcode_stock', models.CharField(blank=True, max_length=20, null=True)),
                ('sup_code', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=15)),
                ('locationbase', models.IntegerField()),
                ('barcode', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('fdate', models.DateField()),
                ('tdate', models.DateField()),
                ('sa_type_a', models.IntegerField()),
                ('sa_type_h', models.IntegerField()),
                ('qtyr', models.IntegerField()),
                ('ato', models.IntegerField()),
                ('product_img', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Product',
                'db_table': 'ali_product',
                'ordering': ('pcode',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=250)),
                ('bf_ref', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Product Category',
                'db_table': 'ali_productgroup',
            },
        ),
        migrations.CreateModel(
            name='SaleInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(max_length=255)),
                ('pano', models.CharField(max_length=255)),
                ('sadate', models.CharField(max_length=255)),
                ('sctime', models.DateTimeField()),
                ('inv_code', models.CharField(max_length=255)),
                ('inv_ref', models.CharField(max_length=255)),
                ('mcode', models.CharField(max_length=255)),
                ('sp_code', models.CharField(max_length=255)),
                ('sp_pos', models.CharField(max_length=10)),
                ('name_f', models.CharField(max_length=255)),
                ('name_t', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_vat', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_net', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_invat', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_exvat', models.DecimalField(decimal_places=2, max_digits=15)),
                ('customer_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('tot_pv', models.CharField(max_length=255)),
                ('tot_bv', models.CharField(max_length=255)),
                ('tot_fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('tot_sppv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('tot_weight', models.DecimalField(decimal_places=2, max_digits=15)),
                ('usercode', models.CharField(max_length=255)),
                ('remark', models.CharField(max_length=255)),
                ('trnf', models.IntegerField(blank=True, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('uid', models.CharField(max_length=255)),
                ('uid_branch', models.CharField(max_length=20)),
                ('lid', models.CharField(max_length=255)),
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
                ('chkcredit4', models.CharField(db_column='chkCredit4', max_length=255)),
                ('chkinternet', models.CharField(db_column='chkInternet', max_length=255)),
                ('chkdiscount', models.CharField(db_column='chkDiscount', max_length=255)),
                ('chkother', models.CharField(db_column='chkOther', max_length=255)),
                ('txtcash', models.DecimalField(db_column='txtCash', decimal_places=2, max_digits=15)),
                ('txtfuture', models.DecimalField(db_column='txtFuture', decimal_places=2, max_digits=15)),
                ('txttransfer', models.DecimalField(db_column='txtTransfer', decimal_places=2, max_digits=15)),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('txtcredit1', models.DecimalField(db_column='txtCredit1', decimal_places=2, max_digits=15)),
                ('txtcredit2', models.DecimalField(db_column='txtCredit2', decimal_places=2, max_digits=15)),
                ('txtcredit3', models.DecimalField(db_column='txtCredit3', decimal_places=2, max_digits=15)),
                ('txtcredit4', models.DecimalField(db_column='txtCredit4', decimal_places=2, max_digits=15)),
                ('txtinternet', models.DecimalField(db_column='txtInternet', decimal_places=2, max_digits=15)),
                ('txtdiscount', models.DecimalField(db_column='txtDiscount', decimal_places=2, max_digits=15)),
                ('txtother', models.DecimalField(db_column='txtOther', decimal_places=2, max_digits=15)),
                ('txtsending', models.DecimalField(db_column='txtSending', decimal_places=2, max_digits=15)),
                ('optioncash', models.CharField(db_column='optionCash', max_length=255)),
                ('optionfuture', models.CharField(db_column='optionFuture', max_length=255)),
                ('optiontransfer', models.CharField(db_column='optionTransfer', max_length=255)),
                ('optioncredit1', models.CharField(db_column='optionCredit1', max_length=255)),
                ('optioncredit2', models.CharField(db_column='optionCredit2', max_length=255)),
                ('optioncredit3', models.CharField(db_column='optionCredit3', max_length=255)),
                ('optioncredit4', models.CharField(db_column='optionCredit4', max_length=255)),
                ('optioninternet', models.CharField(db_column='optionInternet', max_length=255)),
                ('optiondiscount', models.CharField(db_column='optionDiscount', max_length=255)),
                ('optionother', models.CharField(db_column='optionOther', max_length=255)),
                ('discount', models.CharField(max_length=255)),
                ('print', models.IntegerField()),
                ('ewallet_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ipay', models.CharField(max_length=255)),
                ('pay_type', models.CharField(max_length=255)),
                ('hcancel', models.IntegerField()),
                ('caddress', models.TextField()),
                ('cdistrictid', models.CharField(db_column='cdistrictId', max_length=255)),
                ('camphurid', models.CharField(db_column='camphurId', max_length=255)),
                ('cprovinceid', models.CharField(db_column='cprovinceId', max_length=255)),
                ('czip', models.CharField(max_length=255)),
                ('sender', models.IntegerField()),
                ('sender_date', models.DateField()),
                ('receive', models.IntegerField()),
                ('receive_date', models.DateField()),
                ('asend', models.IntegerField()),
                ('ato_type', models.IntegerField()),
                ('ato_id', models.IntegerField()),
                ('online', models.IntegerField()),
                ('hpv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('htotal', models.DecimalField(decimal_places=2, max_digits=15)),
                ('hdate', models.DateField()),
                ('scheck', models.CharField(max_length=255)),
                ('checkportal', models.IntegerField()),
                ('rcode', models.IntegerField()),
                ('bmcauto', models.IntegerField()),
                ('cancel_date', models.DateTimeField()),
                ('uid_cancel', models.CharField(max_length=255)),
                ('cname', models.CharField(max_length=255)),
                ('cmobile', models.CharField(max_length=255)),
                ('uid_sender', models.CharField(max_length=255)),
                ('uid_receive', models.CharField(max_length=255)),
                ('mbase', models.CharField(max_length=255)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('locationbase', models.IntegerField()),
                ('crate', models.DecimalField(decimal_places=6, max_digits=11)),
                ('status', models.IntegerField()),
                ('ref', models.CharField(max_length=100)),
                ('selectcash', models.CharField(db_column='selectCash', max_length=255)),
                ('selecttransfer', models.CharField(db_column='selectTransfer', max_length=255)),
                ('selectcredit1', models.CharField(db_column='selectCredit1', max_length=255)),
                ('selectcredit2', models.CharField(db_column='selectCredit2', max_length=255)),
                ('selectcredit3', models.CharField(db_column='selectCredit3', max_length=255)),
                ('selectdiscount', models.CharField(db_column='selectDiscount', max_length=255)),
                ('selectinternet', models.CharField(db_column='selectInternet', max_length=255)),
                ('txtvoucher', models.DecimalField(db_column='txtVoucher', decimal_places=2, max_digits=15)),
                ('optionvoucher', models.CharField(db_column='optionVoucher', max_length=255)),
                ('selectvoucher', models.CharField(db_column='selectVoucher', max_length=255)),
                ('txttransfer1', models.CharField(db_column='txtTransfer1', max_length=255)),
                ('optiontransfer1', models.CharField(db_column='optionTransfer1', max_length=255)),
                ('selecttransfer1', models.CharField(db_column='selectTransfer1', max_length=255)),
                ('txttransfer2', models.CharField(db_column='txtTransfer2', max_length=255)),
                ('optiontransfer2', models.CharField(db_column='optionTransfer2', max_length=255)),
                ('selecttransfer2', models.CharField(db_column='selectTransfer2', max_length=255)),
                ('txttransfer3', models.CharField(db_column='txtTransfer3', max_length=255)),
                ('optiontransfer3', models.CharField(db_column='optionTransfer3', max_length=255)),
                ('selecttransfer3', models.CharField(db_column='selectTransfer3', max_length=255)),
                ('status_package', models.IntegerField()),
                ('txtpremium', models.DecimalField(blank=True, db_column='txtPremium', decimal_places=2, max_digits=15, null=True)),
                ('chkpremium', models.CharField(blank=True, db_column='chkPremium', max_length=8, null=True)),
                ('selectpremium', models.CharField(blank=True, db_column='selectPremium', max_length=8, null=True)),
                ('optionpremium', models.CharField(blank=True, db_column='optionPremium', max_length=128, null=True)),
            ],
            options={
                'verbose_name_plural': 'Sale Invoice',
                'db_table': 'ali_asaleh',
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=7, null=True)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('pcode', models.CharField(blank=True, max_length=20, null=True)),
                ('pdesc', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(max_length=255)),
                ('mcode', models.CharField(blank=True, max_length=255, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('customer_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('pv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('sppv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('fv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('uidbase', models.CharField(max_length=255)),
                ('locationbase', models.IntegerField()),
                ('outstanding', models.CharField(max_length=255)),
                ('vat', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Sale Item',
                'db_table': 'ali_asaled',
            },
        ),
        migrations.CreateModel(
            name='Ewallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('rcode', models.IntegerField()),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('mcode', models.CharField(blank=True, max_length=255, null=True)),
                ('name_f', models.CharField(max_length=255)),
                ('name_t', models.CharField(max_length=255)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('usercode', models.CharField(blank=True, max_length=3, null=True)),
                ('remark', models.CharField(max_length=255)),
                ('trnf', models.CharField(blank=True, max_length=1, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('uid', models.CharField(max_length=255)),
                ('lid', models.CharField(max_length=255)),
                ('dl', models.CharField(max_length=1)),
                ('cancel', models.IntegerField()),
                ('send', models.IntegerField()),
                ('txtmoney', models.DecimalField(db_column='txtMoney', decimal_places=2, max_digits=15)),
                ('chkcash', models.CharField(db_column='chkCash', max_length=255)),
                ('chkinternet', models.CharField(db_column='chkInternet', max_length=100)),
                ('chkfuture', models.CharField(db_column='chkFuture', max_length=255)),
                ('chktransfer', models.CharField(db_column='chkTransfer', max_length=255)),
                ('chkcredit1', models.CharField(db_column='chkCredit1', max_length=255)),
                ('chkcredit2', models.CharField(db_column='chkCredit2', max_length=255)),
                ('chkcredit3', models.CharField(db_column='chkCredit3', max_length=255)),
                ('chkwithdraw', models.CharField(db_column='chkWithdraw', max_length=255)),
                ('txtdiscount', models.DecimalField(db_column='txtDiscount', decimal_places=2, max_digits=15)),
                ('chktransfer_in', models.CharField(db_column='chkTransfer_in', max_length=255)),
                ('chktransfer_out', models.CharField(db_column='chkTransfer_out', max_length=255)),
                ('txtcash', models.DecimalField(db_column='txtCash', decimal_places=2, max_digits=15)),
                ('txtfuture', models.DecimalField(db_column='txtFuture', decimal_places=2, max_digits=15)),
                ('txtinternet', models.DecimalField(db_column='txtInternet', decimal_places=2, max_digits=15)),
                ('txttransfer', models.DecimalField(db_column='txtTransfer', decimal_places=2, max_digits=15)),
                ('txtcredit1', models.DecimalField(db_column='txtCredit1', decimal_places=2, max_digits=15)),
                ('txtcredit2', models.DecimalField(db_column='txtCredit2', decimal_places=2, max_digits=15)),
                ('txtcredit3', models.DecimalField(db_column='txtCredit3', decimal_places=2, max_digits=15)),
                ('txtwithdraw', models.DecimalField(db_column='txtWithdraw', decimal_places=2, max_digits=15)),
                ('txttransfer_in', models.DecimalField(db_column='txtTransfer_in', decimal_places=2, max_digits=15)),
                ('txttransfer_out', models.DecimalField(db_column='txtTransfer_out', decimal_places=2, max_digits=15)),
                ('optioncash', models.CharField(db_column='optionCash', max_length=255)),
                ('optionfuture', models.CharField(db_column='optionFuture', max_length=255)),
                ('optiontransfer', models.CharField(db_column='optionTransfer', max_length=255)),
                ('optioncredit1', models.CharField(db_column='optionCredit1', max_length=255)),
                ('optioncredit2', models.CharField(db_column='optionCredit2', max_length=255)),
                ('optioncredit3', models.CharField(db_column='optionCredit3', max_length=255)),
                ('optionwithdraw', models.CharField(db_column='optionWithdraw', max_length=255)),
                ('optiontransfer_in', models.CharField(db_column='optionTransfer_in', max_length=255)),
                ('optiontransfer_out', models.CharField(db_column='optionTransfer_out', max_length=255)),
                ('txtoption', models.TextField()),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ipay', models.CharField(max_length=255)),
                ('checkportal', models.IntegerField()),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cancel_date', models.DateField()),
                ('uid_cancel', models.CharField(max_length=255)),
                ('locationbase', models.IntegerField()),
                ('chkcommission', models.CharField(db_column='chkCommission', max_length=255)),
                ('txtcommission', models.DecimalField(db_column='txtCommission', decimal_places=2, max_digits=15)),
                ('optioncommission', models.CharField(db_column='optionCommission', max_length=255)),
                ('mbase', models.CharField(max_length=244)),
                ('crate', models.DecimalField(decimal_places=6, max_digits=11)),
                ('echeck', models.CharField(max_length=255)),
                ('sano_temp', models.CharField(max_length=255)),
                ('selectcash', models.CharField(blank=True, db_column='selectCash', max_length=255, null=True)),
                ('selecttransfer', models.CharField(blank=True, db_column='selectTransfer', max_length=255, null=True)),
                ('selectcredit1', models.CharField(blank=True, db_column='selectCredit1', max_length=255, null=True)),
                ('selectcredit2', models.CharField(blank=True, db_column='selectCredit2', max_length=255, null=True)),
                ('selectcredit3', models.CharField(blank=True, db_column='selectCredit3', max_length=255, null=True)),
                ('optioninternet', models.CharField(blank=True, db_column='optionInternet', max_length=255, null=True)),
                ('selectinternet', models.CharField(blank=True, db_column='selectInternet', max_length=255, null=True)),
                ('txttransfer1',
                 models.DecimalField(blank=True, db_column='txtTransfer1', decimal_places=2, max_digits=15, null=True)),
                ('optiontransfer1',
                 models.CharField(blank=True, db_column='optionTransfer1', max_length=255, null=True)),
                ('selecttransfer1',
                 models.CharField(blank=True, db_column='selectTransfer1', max_length=255, null=True)),
                ('txttransfer2',
                 models.DecimalField(blank=True, db_column='txtTransfer2', decimal_places=2, max_digits=15, null=True)),
                ('optiontransfer2',
                 models.CharField(blank=True, db_column='optionTransfer2', max_length=255, null=True)),
                ('selecttransfer2',
                 models.CharField(blank=True, db_column='selectTransfer2', max_length=255, null=True)),
                ('txttransfer3',
                 models.DecimalField(blank=True, db_column='txtTransfer3', decimal_places=2, max_digits=15, null=True)),
                ('optiontransfer3',
                 models.CharField(blank=True, db_column='optionTransfer3', max_length=255, null=True)),
                ('selecttransfer3',
                 models.CharField(blank=True, db_column='selectTransfer3', max_length=255, null=True)),
                ('image_transfer', models.TextField()),
                ('txtvoucher', models.DecimalField(db_column='txtVoucher', decimal_places=2, max_digits=15)),
                ('id_ecom', models.CharField(max_length=255)),
                ('cals', models.CharField(max_length=255)),
                ('txtpremium',
                 models.DecimalField(blank=True, db_column='txtPremium', decimal_places=2, max_digits=15, null=True)),
                ('chkpremium', models.CharField(blank=True, db_column='chkPremium', max_length=8, null=True)),
                ('selectpremium', models.CharField(blank=True, db_column='selectPremium', max_length=8, null=True)),
                ('optionpremium', models.CharField(blank=True, db_column='optionPremium', max_length=128, null=True)),
            ],
            options={
                'db_table': 'ali_ewallet',
            },
        ),
        migrations.CreateModel(
            name='Eatoship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sano', models.CharField(blank=True, max_length=255, null=True)),
                ('sadate', models.DateField(blank=True, null=True)),
                ('inv_code', models.CharField(blank=True, max_length=255, null=True)),
                ('mcode', models.CharField(blank=True, max_length=255, null=True)),
                ('name_f', models.CharField(max_length=255)),
                ('name_t', models.CharField(max_length=255)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('pv', models.IntegerField()),
                ('usercode', models.CharField(blank=True, max_length=3, null=True)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('trnf', models.CharField(blank=True, max_length=1, null=True)),
                ('sa_type', models.CharField(max_length=2)),
                ('uid', models.CharField(max_length=255)),
                ('lid', models.CharField(max_length=255)),
                ('dl', models.CharField(max_length=1)),
                ('cancel', models.IntegerField()),
                ('send', models.IntegerField()),
                ('txtmoney', models.DecimalField(db_column='txtMoney', decimal_places=2, max_digits=15)),
                ('chkcash', models.CharField(db_column='chkCash', max_length=255)),
                ('chkfuture', models.CharField(db_column='chkFuture', max_length=255)),
                ('chkinternet', models.CharField(db_column='chkInternet', max_length=100)),
                ('chktransfer', models.CharField(db_column='chkTransfer', max_length=255)),
                ('chkcredit1', models.CharField(db_column='chkCredit1', max_length=255)),
                ('chkcredit2', models.CharField(db_column='chkCredit2', max_length=255)),
                ('chkcredit3', models.CharField(db_column='chkCredit3', max_length=255)),
                ('chkwithdraw', models.CharField(db_column='chkWithdraw', max_length=255)),
                ('chktransfer_in', models.CharField(db_column='chkTransfer_in', max_length=255)),
                ('chktransfer_out', models.CharField(db_column='chkTransfer_out', max_length=255)),
                ('txtcash', models.DecimalField(db_column='txtCash', decimal_places=3, max_digits=15)),
                ('txtfuture', models.DecimalField(db_column='txtFuture', decimal_places=3, max_digits=15)),
                ('txtinternet', models.DecimalField(db_column='txtInternet', decimal_places=2, max_digits=15)),
                ('txttransfer', models.DecimalField(db_column='txtTransfer', decimal_places=3, max_digits=15)),
                ('txtcredit1', models.DecimalField(db_column='txtCredit1', decimal_places=3, max_digits=15)),
                ('txtcredit2', models.DecimalField(db_column='txtCredit2', decimal_places=3, max_digits=15)),
                ('txtcredit3', models.DecimalField(db_column='txtCredit3', decimal_places=3, max_digits=15)),
                ('txtwithdraw', models.DecimalField(db_column='txtWithdraw', decimal_places=3, max_digits=15)),
                ('txtdiscount', models.DecimalField(db_column='txtDiscount', decimal_places=2, max_digits=15)),
                ('txttransfer_in', models.DecimalField(db_column='txtTransfer_in', decimal_places=3, max_digits=15)),
                ('txttransfer_out', models.DecimalField(db_column='txtTransfer_out', decimal_places=3, max_digits=15)),
                ('txtvoucher', models.CharField(db_column='txtVoucher', max_length=255)),
                ('optioncash', models.CharField(db_column='optionCash', max_length=255)),
                ('optionfuture', models.CharField(db_column='optionFuture', max_length=255)),
                ('optiontransfer', models.CharField(db_column='optionTransfer', max_length=255)),
                ('optioncredit1', models.CharField(db_column='optionCredit1', max_length=255)),
                ('optioncredit2', models.CharField(db_column='optionCredit2', max_length=255)),
                ('optioncredit3', models.CharField(db_column='optionCredit3', max_length=255)),
                ('optionwithdraw', models.CharField(db_column='optionWithdraw', max_length=255)),
                ('optiontransfer_in', models.CharField(db_column='optionTransfer_in', max_length=255)),
                ('optiontransfer_out', models.CharField(db_column='optionTransfer_out', max_length=255)),
                ('txtoption', models.TextField()),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_before', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ewallet_after', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ipay', models.CharField(max_length=255)),
                ('checkportal', models.IntegerField()),
                ('bprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cancel_date', models.DateField()),
                ('uid_cancel', models.CharField(max_length=255)),
                ('locationbase', models.IntegerField()),
                ('chkcommission', models.CharField(db_column='chkCommission', max_length=255)),
                ('txtcommission', models.DecimalField(db_column='txtCommission', decimal_places=2, max_digits=15)),
                ('optioncommission', models.CharField(db_column='optionCommission', max_length=255)),
                ('mbase', models.CharField(max_length=244)),
                ('crate', models.DecimalField(decimal_places=6, max_digits=11)),
                ('rcode', models.IntegerField()),
                ('echeck', models.CharField(max_length=255)),
                ('txtpremium',
                 models.DecimalField(blank=True, db_column='txtPremium', decimal_places=2, max_digits=15, null=True)),
                ('chkpremium', models.CharField(blank=True, db_column='chkPremium', max_length=8, null=True)),
                ('selectpremium', models.CharField(blank=True, db_column='selectPremium', max_length=8, null=True)),
                ('optionpremium', models.CharField(blank=True, db_column='optionPremium', max_length=128, null=True)),
            ],
            options={
                'db_table': 'ali_eatoship',
            },
        ),
    ]
