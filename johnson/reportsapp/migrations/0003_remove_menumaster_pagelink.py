# Generated by Django 4.0.4 on 2022-11-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0002_menumaster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menumaster',
            name='pagelink',
        ),
    ]
