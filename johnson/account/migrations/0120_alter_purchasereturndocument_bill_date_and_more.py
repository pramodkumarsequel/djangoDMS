# Generated by Django 4.0.4 on 2023-04-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0119_purchaseinvoice_mrn_date_purchaseinvoice_mrn_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasereturndocument',
            name='Bill_Date',
            field=models.DateField(verbose_name='PR Order Date'),
        ),
        migrations.AlterField(
            model_name='purchasereturndocument',
            name='SAP_Order_No',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PR Order No'),
        ),
    ]
