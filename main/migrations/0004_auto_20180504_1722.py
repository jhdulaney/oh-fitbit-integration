# Generated by Django 2.0.4 on 2018-05-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180430_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitbitmember',
            name='last_submitted',
            field=models.DateTimeField(default='2018-04-27 17:22:52+00:00'),
        ),
        migrations.AddField(
            model_name='fitbitmember',
            name='last_updated',
            field=models.DateTimeField(default='2018-04-27 17:22:52+00:00'),
        ),
    ]
