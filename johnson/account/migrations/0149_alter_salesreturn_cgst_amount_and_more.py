# Generated by Django 4.0.4 on 2023-05-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0148_alter_delivery_note_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesreturn',
            name='CGST_AMOUNT',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='Cash_Discount_Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='IGST_AMOUNT',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='RO_Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='SGST_AMOUNT',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='Total_GST',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='Total_Inventory_Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='salesreturn',
            name='Total_Invoice_Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Total Invoice Amount'),
        ),
    ]
