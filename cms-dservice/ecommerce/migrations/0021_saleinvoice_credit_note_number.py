# Generated by Django 2.1.3 on 2019-01-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0020_link_promotion_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleinvoice',
            name='credit_note_number',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
