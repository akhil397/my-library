# Generated by Django 4.0.1 on 2022-12-12 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartpage', '0009_delete_purchasdatamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasmodel',
            name='BName',
        ),
    ]
