# Generated by Django 3.2.6 on 2021-08-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_app', '0003_alter_data_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='priceSP',
            field=models.FloatField(),
        ),
    ]