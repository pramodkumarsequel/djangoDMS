# Generated by Django 4.0.4 on 2023-02-06 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_remove_stock_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 2, 6, 15, 2, 10, 105545)),
            preserve_default=False,
        ),
    ]
