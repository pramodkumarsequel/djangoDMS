# Generated by Django 4.0.4 on 2022-10-17 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_item_taxrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='TaxRate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.taxmaster', verbose_name='Tax Rate'),
        ),
    ]