# Generated by Django 4.0.4 on 2023-04-03 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0114_alter_purchasedocument_sap_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt_note',
            name='billing_entity',
            field=models.CharField(choices=[('Johnson and Johnson Surgical Vision India Pvt. Ltd.', 'Johnson and Johnson Surgical Vision India Pvt. Ltd.'), ('Johnson and Johnson .', 'Johnson and Johnson ')], default=1, max_length=100, verbose_name='Billing Entity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt_note',
            name='supplier_invoice_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 3, 17, 50, 25, 796975), verbose_name='Supplier Invoice Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receipt_note',
            name='Invoice_No',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Supplier Invoice No'),
        ),
    ]
