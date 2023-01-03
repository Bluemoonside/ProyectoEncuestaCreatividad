# Generated by Django 4.1.4 on 2023-01-02 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0016_merge_20230102_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dimension',
            name='indicators',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='dimension',
            name='variables',
            field=models.ManyToManyField(to='Models.variable'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='dimensions',
            field=models.ManyToManyField(to='Models.dimension'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 15, 3, 11, 216707), verbose_name='date published'),
        ),
    ]