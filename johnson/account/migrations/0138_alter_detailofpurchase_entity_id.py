# Generated by Django 4.0.4 on 2023-04-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0137_alter_delivery_note_delivery_note_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailofpurchase',
            name='entity_id',
            field=models.IntegerField(default=48, verbose_name='TID'),
            preserve_default=False,
        ),
    ]