# Generated by Django 3.1.5 on 2021-02-21 00:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 0, 19, 18, 207403, tzinfo=utc)),
        ),
    ]