# Generated by Django 4.0.4 on 2023-04-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0123_alter_purchasereturndocument_igst_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Distributors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.distributor', verbose_name='Distributor Code'),
        ),
    ]
