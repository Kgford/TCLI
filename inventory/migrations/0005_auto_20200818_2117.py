# Generated by Django 3.0.8 on 2020-08-19 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200816_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='inventory_id',
            field=models.IntegerField(null=True),
        ),
    ]