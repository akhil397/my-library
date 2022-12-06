# Generated by Django 4.0.2 on 2022-10-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(max_length=30)),
                ('CPhone', models.CharField(max_length=10)),
                ('CMail', models.EmailField(max_length=254)),
                ('CAddress', models.CharField(max_length=50)),
                ('CDistric', models.CharField(default='', max_length=100)),
                ('CBranch', models.CharField(default='', max_length=100)),
                ('CZipcode', models.CharField(max_length=6)),
                ('Ddate', models.DateField()),
                ('Dtime', models.TimeField()),
            ],
        ),
    ]