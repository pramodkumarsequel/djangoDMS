# Generated by Django 4.0.4 on 2023-02-06 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0044_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='created_on',
        ),
    ]
