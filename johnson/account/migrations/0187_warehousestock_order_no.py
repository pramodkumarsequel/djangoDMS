# Generated by Django 4.0.4 on 2023-07-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0186_warehouseitemchild_item_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehousestock',
            name='order_no',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Stock ID'),
        ),
    ]
