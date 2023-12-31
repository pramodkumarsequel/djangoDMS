# Generated by Django 4.0.4 on 2023-07-30 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0212_alter_detailofpurchase_bal_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closing_balance', models.CharField(max_length=100, verbose_name='Closing Balance')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.item', verbose_name='Item')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.warehouse', verbose_name='Warehouse')),
            ],
        ),
    ]
