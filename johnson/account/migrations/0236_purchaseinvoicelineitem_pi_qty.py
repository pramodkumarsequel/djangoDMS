# Generated by Django 4.0.4 on 2023-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0235_receipt_note_detail_mrn_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoicelineitem',
            name='PI_QTY',
            field=models.IntegerField(default=0),
        ),
    ]
