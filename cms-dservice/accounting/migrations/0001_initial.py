# Generated by Django 2.1.3 on 2019-02-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
        migrations.CreateModel(
            name='StatementState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=64)),
                ('code', models.CharField(default=' ', max_length=4)),
                ('use_app', models.CharField(default=' ', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=64)),
                ('code', models.CharField(default=' ', max_length=4)),
                ('use_app', models.CharField(default=' ', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
