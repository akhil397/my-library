# Generated by Django 4.0.1 on 2022-12-12 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartpage', '0008_remove_purchasdatamodel_bname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchasDataModel',
        ),
    ]
