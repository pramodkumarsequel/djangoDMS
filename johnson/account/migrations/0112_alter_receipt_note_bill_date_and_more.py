# Generated by Django 4.0.4 on 2023-04-03 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0111_alter_receipt_note_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_note',
            name='Bill_Date',
            field=models.DateField(verbose_name='Purchase Order Date'),
        ),
        migrations.AlterField(
            model_name='receipt_note',
            name='order_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.purchasedocument', verbose_name='Purchase Order Number'),
        ),
    ]
