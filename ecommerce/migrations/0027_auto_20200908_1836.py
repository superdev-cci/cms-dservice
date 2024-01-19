# Generated by Django 2.1.3 on 2020-09-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0026_shippingbox_space_margin'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleinvoice',
            name='chktc',
            field=models.CharField(blank=True, db_column='chktc', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='saleinvoice',
            name='optiontc',
            field=models.CharField(blank=True, db_column='optiontc', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='saleinvoice',
            name='selecttc',
            field=models.CharField(blank=True, db_column='selecttc', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='saleinvoice',
            name='txttc',
            field=models.DecimalField(blank=True, db_column='txttc', decimal_places=2, max_digits=15, null=True),
        ),
    ]
