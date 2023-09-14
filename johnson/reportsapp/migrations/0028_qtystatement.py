# Generated by Django 4.0.4 on 2023-06-19 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0160_alter_delivery_note_details_entity_id'),
        ('reportsapp', '0027_alter_stockstatement_uom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qtystatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=50, verbose_name='Document Type')),
                ('docid', models.IntegerField(default=0, verbose_name='Document ID')),
                ('doc_date', models.DateField(verbose_name='Document Date')),
                ('warehouse_name', models.CharField(max_length=50, verbose_name='Warehouse Name')),
                ('item_name', models.CharField(max_length=50, verbose_name='Item Name')),
                ('Qty', models.IntegerField(default=0, verbose_name='Quantity')),
                ('uom', models.CharField(max_length=50, null=True, verbose_name='UOM')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.item', verbose_name='Item ID')),
                ('warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.warehouse', verbose_name='Warehouse ID')),
            ],
        ),
    ]
