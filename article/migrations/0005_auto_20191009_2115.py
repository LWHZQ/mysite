# Generated by Django 2.1.7 on 2019-10-09 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20191009_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 9, 13, 15, 34, 505220, tzinfo=utc)),
        ),
    ]