# Generated by Django 4.0.4 on 2023-05-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0145_purchasereturndocument_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousestock',
            name='Date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
