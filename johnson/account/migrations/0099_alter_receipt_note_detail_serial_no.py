# Generated by Django 4.0.4 on 2023-03-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0098_alter_receipt_note_total_gst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_note_detail',
            name='Serial_No',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Serial No'),
        ),
    ]
