# Generated by Django 4.0.4 on 2023-08-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0246_alter_warehousestock_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]