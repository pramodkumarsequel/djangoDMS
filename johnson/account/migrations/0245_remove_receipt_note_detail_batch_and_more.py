# Generated by Django 4.0.4 on 2023-08-28 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0244_remove_purchasedocument_sap_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt_note_detail',
            name='Batch',
        ),
        migrations.RemoveField(
            model_name='receipt_note_detail',
            name='Reference_No',
        ),
    ]
