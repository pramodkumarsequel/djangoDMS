# Generated by Django 4.0.4 on 2023-06-20 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0165_remove_item_purchase_uom_remove_item_sale_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='purchase_uom',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='sale_unit_p', to='account.uom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='sale_uom',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='sale_unit_m', to='account.uom'),
            preserve_default=False,
        ),
    ]
