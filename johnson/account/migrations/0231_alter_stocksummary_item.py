# Generated by Django 4.0.4 on 2023-08-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0230_stocksummary_itm_code_stocksummary_w_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocksummary',
            name='item',
            field=models.IntegerField(default=0, verbose_name='Item'),
        ),
    ]
