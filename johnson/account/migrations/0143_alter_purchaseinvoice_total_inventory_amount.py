# Generated by Django 4.0.4 on 2023-05-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0142_alter_purchaseinvoice_cgst_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='Total_Inventory_Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Total Inventory Amount'),
        ),
    ]