# Generated by Django 4.0.4 on 2023-07-18 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0191_remove_receipt_note_detail_receiptnotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseinvoicelineitem',
            name='Total_Amounts',
        ),
    ]
