# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import tuesmon.users.models
import uuid


def update_uuids(apps, schema_editor):
    User = apps.get_model("users", "User")
    for user in User.objects.all():
        user.uuid = uuid.uuid4().hex
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20170406_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=tuesmon.users.models.get_default_uuid, editable=False, max_length=32),
        ),
        migrations.RunPython(update_uuids, lambda apps, schema_editor: None),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=tuesmon.users.models.get_default_uuid, editable=False, max_length=32, unique=True),
        ),
    ]
