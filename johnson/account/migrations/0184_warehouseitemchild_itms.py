# Generated by Django 4.0.4 on 2023-07-14 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0183_remove_warehouseitemchild_item_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseitemchild',
            name='itms',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, to='account.item', verbose_name='Item_Code'),
            preserve_default=False,
        ),
    ]