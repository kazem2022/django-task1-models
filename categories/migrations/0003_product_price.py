# Generated by Django 4.2.7 on 2023-12-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_producer_brand_rename_producer_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
