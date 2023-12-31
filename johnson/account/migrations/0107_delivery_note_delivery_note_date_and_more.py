# Generated by Django 4.0.4 on 2023-04-03 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0106_sales_sales_order_no_alter_sales_invoice_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_note',
            name='delivery_note_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 3, 9, 41, 14, 354204), verbose_name='Delivery Note Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery_note',
            name='delivery_note_no',
            field=models.CharField(default='DMS', max_length=50, verbose_name='Delivery Note No'),
            preserve_default=False,
        ),
    ]
