# Generated by Django 4.0.4 on 2023-08-02 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0216_alter_stocksummary_closing_balance_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='stockSummary',
        ),
    ]
