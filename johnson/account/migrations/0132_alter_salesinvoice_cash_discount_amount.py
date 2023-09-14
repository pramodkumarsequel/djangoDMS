# Generated by Django 4.0.4 on 2023-04-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0131_remove_salesreturn_invoice_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='Cash_Discount_Amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='Total Discount Amount'),
        ),
    ]