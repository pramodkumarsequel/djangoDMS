# Generated by Django 4.0.4 on 2023-08-16 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0232_stocksummary_op'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt_note',
            old_name='order_no',
            new_name='p_order_no',
        ),
    ]
