# Generated by Django 4.0.4 on 2023-07-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0178_remove_salesreturn_current_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citymaster',
            name='City_Name',
            field=models.CharField(max_length=50, unique=True, verbose_name='City Name'),
        ),
        migrations.AlterField(
            model_name='regionmaster',
            name='Region_Name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Region Name'),
        ),
        migrations.AlterField(
            model_name='statemaster',
            name='State_Name',
            field=models.CharField(max_length=50, unique=True, verbose_name='State Name'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
