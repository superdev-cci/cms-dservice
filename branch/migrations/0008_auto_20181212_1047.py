# Generated by Django 2.1.3 on 2018-12-12 03:47

from django.db import migrations


def link_item_to_branch(apps, schema_editor):
    Branch = apps.get_model('branch', 'Branch')
    BranchStock = apps.get_model('branch', 'BranchStock')
    all_branch = {x.inv_code: x for x in Branch.objects.all()}
    for x in BranchStock.objects.all():
        x.branch = all_branch.get(x.inv_code, None)
        x.save()
    return


def link_item_to_product(apps, schema_editor):
    Product = apps.get_model('ecommerce', 'Product')
    BranchStock = apps.get_model('branch', 'BranchStock')
    all_product = {x.pcode: x for x in Product.objects.all()}
    for x in BranchStock.objects.all():
        x.product = all_product.get(x.pcode, None)
        x.save()
    return


class Migration(migrations.Migration):
    dependencies = [
        ('branch', '0007_auto_20181212_1045'),
    ]

    operations = [
        migrations.RunPython(link_item_to_branch),
        migrations.RunPython(link_item_to_product),
    ]
