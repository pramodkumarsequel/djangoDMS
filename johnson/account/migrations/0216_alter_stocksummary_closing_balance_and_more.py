# Generated by Django 4.0.4 on 2023-08-01 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0215_stocksummary_delivery_child_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocksummary',
            name='closing_balance',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Closing Balance'),
        ),
        migrations.AlterField(
            model_name='stocksummary',
            name='delivery_child_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.delivery_note_details', verbose_name='Delivery Child Order'),
        ),
        migrations.AlterField(
            model_name='stocksummary',
            name='mrn_child_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.receipt_note_detail', verbose_name='Purchase Order Child Item'),
        ),
        migrations.AlterField(
            model_name='stocksummary',
            name='pr_child_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.detailsofpurchasereturn', verbose_name='Purchase Return Child Order'),
        ),
        migrations.AlterField(
            model_name='stocksummary',
            name='sale_return_child_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.sales_return_detail', verbose_name='Sale Return Child Order'),
        ),
    ]
