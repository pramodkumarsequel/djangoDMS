# Generated by Django 4.0.4 on 2023-03-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0060_taxmaster_taxinputrecoverable'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Purchase Price'),
        ),
        migrations.AddField(
            model_name='item',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Sale Price'),
        ),
        migrations.AlterField(
            model_name='item',
            name='MRP',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='Base Price'),
        ),
    ]
