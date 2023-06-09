# Generated by Django 3.2.18 on 2023-05-09 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0004_alter_table_table_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='max_capacity',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_num',
        ),
        migrations.AddField(
            model_name='table',
            name='capacity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='num_of_people',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='table_num',
        ),
        migrations.AddField(
            model_name='booking',
            name='table_num',
            field=models.ManyToManyField(to='booking_system.Table'),
        ),
    ]
