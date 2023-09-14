# Generated by Django 4.0.4 on 2023-04-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0113_delivery_note_details_uom_receipt_note_detail_uom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedocument',
            name='SAP_Order_Date',
            field=models.DateField(blank=True, null=True, verbose_name='Supplier Invoice Date'),
        ),
        migrations.AlterField(
            model_name='purchasedocument',
            name='Supplier_Invoice_No',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier Invoice No'),
        ),
    ]
