# Generated by Django 3.2.6 on 2021-08-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='level1',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='data',
            name='level2',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='data',
            name='level3',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='data',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='data',
            name='priceSP',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
