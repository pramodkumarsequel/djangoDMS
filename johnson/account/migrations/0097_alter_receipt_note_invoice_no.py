# Generated by Django 4.0.4 on 2023-03-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0096_receipt_note_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_note',
            name='Invoice_No',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Order No'),
        ),
    ]