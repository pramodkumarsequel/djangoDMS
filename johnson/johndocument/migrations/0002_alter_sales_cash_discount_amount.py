# Generated by Django 4.0.4 on 2022-05-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('johndocument', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Cash_Discount_Amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
