# Generated by Django 4.0.4 on 2023-05-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0151_alter_purchaseinvoice_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseitemchild',
            name='closingbalance',
            field=models.IntegerField(default=0, verbose_name='Closing Balance'),
        ),
    ]
