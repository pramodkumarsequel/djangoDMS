# Generated by Django 4.0.4 on 2023-03-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0067_purchaseinvoicelineitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoicelineitem',
            name='Rate',
            field=models.FloatField(verbose_name='Rate'),
        ),
    ]