# Generated by Django 4.0.4 on 2022-12-05 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0007_alter_menumaster_dord_alter_menumaster_ismobile_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menumaster',
            options={'ordering': ['Dord']},
        ),
    ]