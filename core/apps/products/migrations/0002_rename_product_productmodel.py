# Generated by Django 5.0.6 on 2024-06-07 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductModel',
        ),
    ]