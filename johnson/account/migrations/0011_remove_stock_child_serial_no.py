# Generated by Django 4.0.4 on 2022-10-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_stock_child_sr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_child',
            name='Serial_No',
        ),
    ]
