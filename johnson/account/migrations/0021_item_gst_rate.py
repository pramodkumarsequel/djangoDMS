# Generated by Django 4.0.4 on 2022-10-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_remove_item_gst_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='GST_Rate',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
