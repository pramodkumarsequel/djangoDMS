# Generated by Django 4.0.4 on 2023-03-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0064_alter_purchasereturndocument_distributor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasereturndocument',
            name='Vendor_Name',
            field=models.CharField(choices=[('Johnson and Johnson Surgical Vision India Pvt. Ltd.', 'Johnson and Johnson Surgical Vision India Pvt. Ltd.'), ('Johnson and Johnson .', 'Johnson and Johnson ')], max_length=100, verbose_name='Billing Entity'),
        ),
    ]
