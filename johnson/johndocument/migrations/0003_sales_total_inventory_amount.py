# Generated by Django 4.0.4 on 2022-05-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('johndocument', '0002_alter_sales_cash_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='Total_Inventory_Amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]