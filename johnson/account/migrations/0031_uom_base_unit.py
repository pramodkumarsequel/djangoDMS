# Generated by Django 4.0.4 on 2022-10-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_unit_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='uom',
            name='base_unit',
            field=models.BooleanField(default=True, verbose_name='Base Unit'),
            preserve_default=False,
        ),
    ]
