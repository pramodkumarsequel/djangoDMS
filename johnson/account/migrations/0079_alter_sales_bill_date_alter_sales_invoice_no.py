# Generated by Django 4.0.4 on 2023-03-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0078_alter_salesinvoice_invoice_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Bill_Date',
            field=models.DateField(verbose_name='Sales Order Date'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Invoice_No',
            field=models.CharField(max_length=50, verbose_name='Sale Order No'),
        ),
    ]
