# Generated by Django 3.2.12 on 2022-05-08 17:04

import names
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ship',
            old_name='mother_ship',
            new_name='mothership',
        ),
        migrations.AlterField(
            model_name='crew',
            name='name',
            field=models.CharField(default=names.get_first_name, max_length=128),
        ),
        migrations.AlterField(
            model_name='mothership',
            name='capacity',
            field=models.IntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='ship',
            name='capacity',
            field=models.IntegerField(default=5),
        ),
    ]
