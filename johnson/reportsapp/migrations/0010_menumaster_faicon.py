# Generated by Django 4.0.4 on 2022-12-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0009_mainmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menumaster',
            name='faicon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
