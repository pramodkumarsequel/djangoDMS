# Generated by Django 4.0.4 on 2023-03-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0086_ordergenerator'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergenerator',
            name='seqnum',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Sequence'),
        ),
    ]