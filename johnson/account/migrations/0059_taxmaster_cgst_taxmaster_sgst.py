# Generated by Django 4.0.4 on 2023-03-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0058_purchasedocument_total_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxmaster',
            name='CGST',
            field=models.DecimalField(decimal_places=2, default=9, max_digits=20, verbose_name='CGST(%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxmaster',
            name='SGST',
            field=models.DecimalField(decimal_places=2, default=7, max_digits=20, verbose_name='SGST(%)'),
            preserve_default=False,
        ),
    ]