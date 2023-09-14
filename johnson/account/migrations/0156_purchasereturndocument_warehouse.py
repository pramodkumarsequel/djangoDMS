# Generated by Django 4.0.4 on 2023-06-15 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0155_salesreturn_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasereturndocument',
            name='warehouse',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='account.warehouse', verbose_name='Warehouse'),
            preserve_default=False,
        ),
    ]
