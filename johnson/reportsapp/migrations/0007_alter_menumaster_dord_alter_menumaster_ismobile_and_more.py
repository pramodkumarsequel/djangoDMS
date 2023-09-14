# Generated by Django 4.0.4 on 2022-11-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0006_menumaster_ismobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumaster',
            name='Dord',
            field=models.IntegerField(blank=True, null=True, verbose_name='Display Order'),
        ),
        migrations.AlterField(
            model_name='menumaster',
            name='IsMobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menumaster',
            name='MTYPE',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Menu Type'),
        ),
    ]
