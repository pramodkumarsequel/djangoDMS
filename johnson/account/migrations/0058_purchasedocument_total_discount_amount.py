# Generated by Django 4.0.4 on 2023-03-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0057_alter_purchasedocument_total_gst'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedocument',
            name='total_discount_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Total Discount Amount'),
            preserve_default=False,
        ),
    ]