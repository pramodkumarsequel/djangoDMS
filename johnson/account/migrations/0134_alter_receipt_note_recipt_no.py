# Generated by Django 4.0.4 on 2023-04-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0133_alter_purchasedocument_sap_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_note',
            name='recipt_no',
            field=models.CharField(max_length=50, unique=True, verbose_name='MRN No'),
        ),
    ]
