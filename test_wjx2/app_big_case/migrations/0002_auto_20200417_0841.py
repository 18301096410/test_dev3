# Generated by Django 2.2.6 on 2020-04-17 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_big_case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinfo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 8, 41, 40, 551886, tzinfo=utc)),
        ),
    ]
