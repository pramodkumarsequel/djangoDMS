# Generated by Django 4.0.4 on 2023-07-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0202_delivery_note_details_bal_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_note_details',
            name='Serial_No',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sales Serial No'),
        ),
    ]