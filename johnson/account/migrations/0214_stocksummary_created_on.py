# Generated by Django 4.0.4 on 2023-08-01 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0213_stocksummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksummary',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 1, 9, 21, 31, 489913)),
            preserve_default=False,
        ),
    ]
