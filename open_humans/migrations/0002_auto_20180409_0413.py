# Generated by Django 2.0.4 on 2018-04-09 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('open_humans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhumansmember',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oh_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
