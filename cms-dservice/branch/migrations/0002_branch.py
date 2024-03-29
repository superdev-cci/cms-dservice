# Generated by Django 2.1.3 on 2018-11-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_code', models.CharField(blank=True, max_length=7, null=True)),
                ('inv_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('inv_type', models.IntegerField()),
                ('code_ref', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('districtid', models.IntegerField(db_column='districtId')),
                ('amphurid', models.IntegerField(db_column='amphurId')),
                ('provinceid', models.IntegerField(db_column='provinceId')),
                ('zip', models.CharField(max_length=5)),
                ('home_t', models.CharField(max_length=255)),
                ('uid', models.IntegerField()),
                ('sync', models.CharField(blank=True, max_length=1, null=True)),
                ('web', models.CharField(blank=True, max_length=1, null=True)),
                ('ewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('voucher', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bewallet', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bvoucher', models.DecimalField(decimal_places=2, max_digits=15)),
                ('discount', models.IntegerField()),
                ('locationbase', models.IntegerField()),
                ('bill_ref', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=10)),
                ('no_tax', models.CharField(max_length=10)),
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 'ali_invent',
            },
        ),
    ]
