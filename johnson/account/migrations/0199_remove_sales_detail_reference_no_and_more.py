# Generated by Django 4.0.4 on 2023-07-19 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0198_remove_detailsofpurchasereturn_details_of_purchase_return_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales_detail',
            name='Reference_No',
        ),
        migrations.RemoveField(
            model_name='sales_detail',
            name='SalesDetails',
        ),
    ]
