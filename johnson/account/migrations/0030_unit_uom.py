# Generated by Django 4.0.4 on 2022-10-28 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_alter_delivery_note_details_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_class', models.CharField(max_length=50, verbose_name='Unit Class')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_notation', models.CharField(max_length=20, unique=True, verbose_name='Unit Notation')),
                ('unit_name', models.CharField(max_length=30, unique=True, verbose_name='Unit Name')),
                ('conversion_factor', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Conversion Factor')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('UNT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.unit', verbose_name='Unit Class')),
            ],
        ),
    ]
