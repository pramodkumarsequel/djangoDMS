# Generated by Django 4.0.4 on 2023-04-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0112_alter_receipt_note_bill_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_note_details',
            name='uom',
            field=models.CharField(max_length=50, null=True, verbose_name='UOM'),
        ),
        migrations.AddField(
            model_name='receipt_note_detail',
            name='uom',
            field=models.CharField(max_length=50, null=True, verbose_name='UOM'),
        ),
    ]
