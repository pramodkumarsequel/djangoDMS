# Generated by Django 4.0.4 on 2023-07-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0180_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='MRP',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Base Price'),
        ),
        migrations.AlterField(
            model_name='ordergenerator',
            name='Document_for_prefix',
            field=models.CharField(blank=True, choices=[('Sales', 'Sales Order'), ('salesInvoice', 'sales Invoice'), ('SalesReturn', 'Sales Return'), ('openingbalance', 'Opening Balance'), ('PurchaseDocument', 'Purchase Order'), ('PurchaseInvoice', 'Purchase Invoice'), ('PurchaseReturnDocument', 'Purchase Return'), ('Delivery_Note', 'Delivery Note'), ('Receipt_Note', 'Matrial Receipt Note')], max_length=30, null=True, verbose_name='Document for prefix'),
        ),
        migrations.AlterField(
            model_name='ordergenerator',
            name='documentType',
            field=models.CharField(choices=[('Sales', 'Sales Order'), ('salesInvoice', 'sales Invoice'), ('SalesReturn', 'Sales Return'), ('openingbalance', 'Opening Balance'), ('PurchaseDocument', 'Purchase Order'), ('PurchaseInvoice', 'Purchase Invoice'), ('PurchaseReturnDocument', 'Purchase Return'), ('Delivery_Note', 'Delivery Note'), ('Receipt_Note', 'Matrial Receipt Note')], max_length=30, unique=True, verbose_name='Document Type'),
        ),
    ]
