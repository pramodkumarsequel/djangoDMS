# Generated by Django 4.0.4 on 2023-03-02 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0049_warehouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='created_at',
        ),
    ]