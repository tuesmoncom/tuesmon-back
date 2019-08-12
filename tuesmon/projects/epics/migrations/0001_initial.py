# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-05 11:12
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tuesmon.projects.notifications.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userstories', '0012_auto_20160614_1201'),
        ('projects', '0049_auto_20160629_1443'),
        ('history', '0012_auto_20160629_1036'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=[], null=True, size=None, verbose_name='tags')),
                ('version', models.IntegerField(default=1, verbose_name='version')),
                ('is_blocked', models.BooleanField(default=False, verbose_name='is blocked')),
                ('blocked_note', models.TextField(blank=True, default='', verbose_name='blocked note')),
                ('ref', models.BigIntegerField(blank=True, db_index=True, default=None, null=True, verbose_name='ref')),
                ('epics_order', models.IntegerField(default=10000, verbose_name='epics order')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date')),
                ('subject', models.TextField(verbose_name='subject')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('client_requirement', models.BooleanField(default=False, verbose_name='is client requirement')),
                ('team_requirement', models.BooleanField(default=False, verbose_name='is team requirement')),
                ('assigned_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='epics_assigned_to_me', to=settings.AUTH_USER_MODEL, verbose_name='assigned to')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_epics', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epics', to='projects.Project', verbose_name='project')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='epics', to='projects.EpicStatus', verbose_name='status')),
            ],
            options={
                'ordering': ['project', 'epics_order', 'ref'],
                'verbose_name_plural': 'epics',
                'verbose_name': 'epic',
            },
            bases=(tuesmon.projects.notifications.mixins.WatchedModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RelatedUserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=10000, verbose_name='order')),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epics.Epic')),
                ('user_story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userstories.UserStory')),
            ],
            options={
                'ordering': ['user_story', 'order', 'id'],
                'verbose_name_plural': 'related user stories',
                'verbose_name': 'related user story',
            },
        ),
        migrations.AddField(
            model_name='epic',
            name='user_stories',
            field=models.ManyToManyField(related_name='epics', through='epics.RelatedUserStory', to='userstories.UserStory', verbose_name='user stories'),
        ),
        # Execute trigger after epic update
        migrations.RunSQL(
            """
            DROP TRIGGER IF EXISTS update_project_tags_colors_on_epic_update ON epics_epic;
            CREATE TRIGGER update_project_tags_colors_on_epic_update
            AFTER UPDATE ON epics_epic
            FOR EACH ROW EXECUTE PROCEDURE update_project_tags_colors();
            """
        ),
        # Execute trigger after epic insert
        migrations.RunSQL(
            """
            DROP TRIGGER IF EXISTS update_project_tags_colors_on_epic_insert ON epics_epic;
            CREATE TRIGGER update_project_tags_colors_on_epic_insert
            AFTER INSERT ON epics_epic
            FOR EACH ROW EXECUTE PROCEDURE update_project_tags_colors();
            """
        ),
    ]
