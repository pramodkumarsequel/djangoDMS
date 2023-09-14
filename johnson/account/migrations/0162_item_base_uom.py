# Generated by Django 4.0.4 on 2023-06-20 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0161_remove_item_base_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='base_uom',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.uom'),
            preserve_default=False,
        ),
    ]
