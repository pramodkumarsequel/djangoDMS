# Generated by Django 4.0.4 on 2023-07-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0195_alter_purchaseinvoicelineitem_serial_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_note_detail',
            name='bal_qty',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='BAL QTY'),
        ),
    ]