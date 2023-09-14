# Generated by Django 4.0.4 on 2023-03-17 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0073_alter_purchaseinvoice_bill_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoice',
            name='purchase_invoice_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 16, 22, 55, 910138), verbose_name='Purchase Invoice Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='purchase_invoice_no',
            field=models.CharField(default=0, max_length=50, verbose_name='Purchase Invoice No'),
            preserve_default=False,
        ),
    ]