# Generated by Django 4.0.4 on 2023-06-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0026_rename_qyn_stockstatement_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockstatement',
            name='uom',
            field=models.CharField(max_length=50, null=True, verbose_name='UOM'),
        ),
    ]
