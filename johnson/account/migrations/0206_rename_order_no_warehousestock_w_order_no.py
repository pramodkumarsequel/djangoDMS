# Generated by Django 4.0.4 on 2023-07-21 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0205_remove_sales_return_detail_reference_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehousestock',
            old_name='order_no',
            new_name='w_order_no',
        ),
    ]
