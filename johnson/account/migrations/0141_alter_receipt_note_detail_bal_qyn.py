# Generated by Django 4.0.4 on 2023-04-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0140_receipt_note_detail_bal_qyn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_note_detail',
            name='bal_qyn',
            field=models.IntegerField(blank=True, null=True, verbose_name='BAL QYN'),
        ),
    ]
