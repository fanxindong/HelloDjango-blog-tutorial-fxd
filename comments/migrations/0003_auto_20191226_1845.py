# Generated by Django 2.2.6 on 2019-12-26 10:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20191218_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 10, 45, 38, 307713, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
