# Generated by Django 4.0.4 on 2023-07-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0210_warehousestock_w_order_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailofpurchase',
            name='bal_qty',
            field=models.IntegerField(default=0, verbose_name='BAL QTY'),
        ),
        migrations.AddField(
            model_name='sales_detail',
            name='bal_qty',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='BAL QTY'),
        ),
    ]
