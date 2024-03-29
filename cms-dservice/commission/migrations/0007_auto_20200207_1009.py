# Generated by Django 2.1.3 on 2020-02-07 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0016_auto_20200207_1009'),
        ('commission', '0006_pvtransfer_create_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='honorchangelog',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AlterField(
            model_name='pvtransfer',
            name='print',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pvtransfer',
            name='rcode',
            field=models.IntegerField(blank=True, default=9, null=True),
        ),
    ]
