# Generated by Django 4.0.4 on 2023-03-17 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0070_saleinvoicelineitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseinvoice',
            name='SAP_Order_No',
        ),
    ]