# Generated by Django 3.2.18 on 2023-04-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_auto_20230407_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_num',
            field=models.IntegerField(unique=True),
        ),
    ]
