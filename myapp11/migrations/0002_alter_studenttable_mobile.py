# Generated by Django 4.1.3 on 2022-11-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp11', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttable',
            name='MObile',
            field=models.IntegerField(),
        ),
    ]
