# Generated by Django 5.0 on 2023-12-27 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0003_historicalperformancemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='vendorapp.vendormodel'),
        ),
    ]
