# Generated by Django 4.0.4 on 2023-08-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0218_stocksummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksummary',
            name='uom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]