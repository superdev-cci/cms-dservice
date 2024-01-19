# Generated by Django 2.1.3 on 2019-02-15 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_payment_paymenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='bprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='customer_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='fv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='locationbase',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='outstanding',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='sano_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ecommerce.SaleInvoice'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='sppv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='uidbase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='unit',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='vat',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='saleinvoice',
            name='sctime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]