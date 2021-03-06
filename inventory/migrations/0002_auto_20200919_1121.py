# Generated by Django 3.0.8 on 2020-09-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='recieved_date',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='shipped_date',
        ),
        migrations.AddField(
            model_name='events',
            name='rtv',
            field=models.CharField(default='N/A', max_length=20, verbose_name='Item Serial number'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.CharField(default='N/A', max_length=50, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.CharField(default='N/A', max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='modelname',
            field=models.CharField(default='N/A', max_length=50, null=True, verbose_name='modelname'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='serial_number',
            field=models.CharField(default='N/A', max_length=50, null=True, verbose_name='serial number'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='shelf',
            field=models.CharField(default='N/A', max_length=10, null=True, verbose_name='shelf'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='status',
            field=models.CharField(default='N/A', max_length=50, null=True, verbose_name='status'),
        ),
    ]
