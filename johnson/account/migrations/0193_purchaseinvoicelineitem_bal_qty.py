# Generated by Django 4.0.4 on 2023-07-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0192_remove_purchaseinvoicelineitem_total_amounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoicelineitem',
            name='bal_qty',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='BAL Qty'),
        ),
    ]
