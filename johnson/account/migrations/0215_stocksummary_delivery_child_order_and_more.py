# Generated by Django 4.0.4 on 2023-08-01 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0214_stocksummary_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksummary',
            name='delivery_child_order',
            field=models.ForeignKey(default=80, on_delete=django.db.models.deletion.CASCADE, to='account.delivery_note_details', verbose_name='Delivery Child Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocksummary',
            name='mrn_child_order',
            field=models.ForeignKey(default=61, on_delete=django.db.models.deletion.CASCADE, to='account.receipt_note_detail', verbose_name='Purchase Order Child Item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocksummary',
            name='pr_child_order',
            field=models.ForeignKey(default=57, on_delete=django.db.models.deletion.CASCADE, to='account.detailsofpurchasereturn', verbose_name='Purchase Return Child Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocksummary',
            name='sale_return_child_order',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to='account.sales_return_detail', verbose_name='Sale Return Child Order'),
            preserve_default=False,
        ),
    ]
