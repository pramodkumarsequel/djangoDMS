# Generated by Django 4.0.4 on 2022-10-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_opening_balance_child_entity_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_note_details',
            name='entity_id',
            field=models.IntegerField(null=True, verbose_name='TID'),
        ),
        migrations.AlterField(
            model_name='detailofpurchase',
            name='entity_id',
            field=models.CharField(max_length=30, null=True, verbose_name='TID'),
        ),
        migrations.AlterField(
            model_name='detailsofpurchasereturn',
            name='entity_id',
            field=models.IntegerField(null=True, verbose_name='TID'),
        ),
        migrations.AlterField(
            model_name='receipt_note_detail',
            name='entity_id',
            field=models.IntegerField(null=True, verbose_name='TID'),
        ),
        migrations.AlterField(
            model_name='stock_child',
            name='entity_id',
            field=models.IntegerField(null=True, verbose_name='TID'),
        ),
    ]
