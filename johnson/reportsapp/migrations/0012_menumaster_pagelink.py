# Generated by Django 4.0.4 on 2022-12-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0011_remove_menumaster_pagelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='menumaster',
            name='pagelink',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Page Link'),
        ),
    ]