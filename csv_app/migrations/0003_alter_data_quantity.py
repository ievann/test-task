# Generated by Django 3.2.6 on 2021-08-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_app', '0002_auto_20210815_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
