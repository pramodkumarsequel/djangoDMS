# Generated by Django 4.0.4 on 2023-07-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0181_alter_item_mrp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseitemchild',
            name='Rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
