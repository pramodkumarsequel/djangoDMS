# Generated by Django 4.0.4 on 2023-03-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0061_item_purchase_price_item_sale_price_alter_item_mrp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousestock',
            name='warehouseName',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Warehouse Name'),
        ),
    ]
