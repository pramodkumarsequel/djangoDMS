# Generated by Django 4.0.4 on 2022-10-12 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_stock_child_serial_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Hierarchy4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Hierarchy5',
        ),
    ]
