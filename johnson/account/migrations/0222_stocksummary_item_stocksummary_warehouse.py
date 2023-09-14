# Generated by Django 4.0.4 on 2023-08-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0221_remove_stocksummary_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksummary',
            name='item',
            field=models.IntegerField(default=0, unique=True, verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='stocksummary',
            name='warehouse',
            field=models.IntegerField(default=0, unique=True, verbose_name='Warehouse'),
        ),
    ]
