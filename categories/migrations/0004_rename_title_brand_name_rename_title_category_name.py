# Generated by Django 4.2.7 on 2023-12-07 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
