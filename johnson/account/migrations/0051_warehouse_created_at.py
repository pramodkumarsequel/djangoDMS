# Generated by Django 4.0.4 on 2023-03-02 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0050_remove_warehouse_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 3, 2, 16, 28, 17, 965526)),
            preserve_default=False,
        ),
    ]
