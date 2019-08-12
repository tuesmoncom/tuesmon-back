# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-28 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tuesmon.base.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0002_epic_color'),
        ('projects', '0050_project_epics_csv_uuid'),
        ('custom_attributes', '0008_auto_20160728_0540'),
    ]

    operations = [
        # Change some verbose names
        migrations.AlterModelOptions(
            name='issuecustomattributesvalues',
            options={'ordering': ['id'], 'verbose_name': 'issue custom attributes values', 'verbose_name_plural': 'issue custom attributes values'},
        ),
        migrations.AlterModelOptions(
            name='taskcustomattributesvalues',
            options={'ordering': ['id'], 'verbose_name': 'task custom attributes values', 'verbose_name_plural': 'task custom attributes values'},
        ),
        migrations.AlterModelOptions(
            name='userstorycustomattributesvalues',
            options={'ordering': ['id'], 'verbose_name': 'user story custom attributes values', 'verbose_name_plural': 'user story custom attributes values'},
        ),
        # Custom attributes for epics
        migrations.CreateModel(
            name='EpicCustomAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('type', models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('date', 'Date'), ('url', 'Url')], default='text', max_length=16, verbose_name='type')),
                ('order', models.IntegerField(default=10000, verbose_name='order')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epiccustomattributes', to='projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'epic custom attribute',
                'abstract': False,
                'ordering': ['project', 'order', 'name'],
                'verbose_name_plural': 'epic custom attributes',
            },
        ),
        migrations.CreateModel(
            name='EpicCustomAttributesValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=1, verbose_name='version')),
                ('attributes_values', tuesmon.base.db.models.fields.JSONField(default={}, verbose_name='values')),
                ('epic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_attributes_values', to='epics.Epic', verbose_name='epic')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'epic custom attributes values',
                'ordering': ['id'],
                'verbose_name_plural': 'epic custom attributes values',
            },
        ),
        migrations.AlterIndexTogether(
            name='epiccustomattributesvalues',
            index_together=set([('epic',)]),
        ),
        migrations.AlterUniqueTogether(
            name='epiccustomattribute',
            unique_together=set([('project', 'name')]),
        ),
        migrations.RunSQL(
            """
            CREATE TRIGGER "update_epiccustomvalues_after_remove_epiccustomattribute"
           AFTER DELETE ON custom_attributes_epiccustomattribute
              FOR EACH ROW
         EXECUTE PROCEDURE clean_key_in_custom_attributes_values('epic_id', 'epics_epic',
                                            'custom_attributes_epiccustomattributesvalues');
            """,
            reverse_sql="""DROP TRIGGER IF EXISTS "update_epiccustomvalues_after_remove_epiccustomattribute"
                                               ON custom_attributes_epiccustomattribute
                                          CASCADE;"""
        ),
    ]
