# Generated by Django 4.0.4 on 2023-03-23 13:48

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0089_remove_ordergenerator_fy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergenerator',
            name='FY',
            field=models.IntegerField(default=account.models.current_year, verbose_name='year'),
        ),
    ]
