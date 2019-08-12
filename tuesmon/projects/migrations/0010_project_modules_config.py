# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tuesmon.base.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20141024_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='modules_config',
            field=tuesmon.base.db.models.fields.JSONField(blank=True, null=True, verbose_name='modules config'),
            preserve_default=True,
        ),
    ]
