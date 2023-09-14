# Generated by Django 4.0.4 on 2023-03-17 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0071_remove_purchaseinvoice_sap_order_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoice',
            name='purchase_invoice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='account.purchasedocument', verbose_name='Purchase Invoice No'),
            preserve_default=False,
        ),
    ]