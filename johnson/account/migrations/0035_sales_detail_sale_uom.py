# Generated by Django 4.0.4 on 2022-11-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_sales_return_detail_sale_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_detail',
            name='sale_uom',
            field=models.CharField(max_length=50, null=True, verbose_name='Sales UOM'),
        ),
    ]
