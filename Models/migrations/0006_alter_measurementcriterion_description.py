# Generated by Django 4.1.4 on 2022-12-24 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0005_alter_dimension_options_alter_indicator_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurementcriterion',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]