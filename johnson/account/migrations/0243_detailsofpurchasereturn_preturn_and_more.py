# Generated by Django 4.0.4 on 2023-08-25 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0242_receipt_note_detail_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsofpurchasereturn',
            name='preturn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.purchasereturndocument'),
        ),
        migrations.AddField(
            model_name='purchaseinvoicelineitem',
            name='pinvoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.purchaseinvoice'),
        ),
        migrations.AddField(
            model_name='warehouseitemchild',
            name='w',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.warehousestock'),
        ),
    ]
