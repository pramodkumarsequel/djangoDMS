# Generated by Django 4.0.4 on 2023-08-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0220_alter_stocksummary_item_alter_stocksummary_warehouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocksummary',
            name='item',
        ),
        migrations.RemoveField(
            model_name='stocksummary',
            name='warehouse',
        ),
    ]
