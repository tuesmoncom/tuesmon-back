# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tuesmon.base.api import serializers
from tuesmon.base.fields import Field, MethodField
from tuesmon.base.neighbors import NeighborsSerializerMixin

from tuesmon.mdrender.service import render as mdrender
from tuesmon.projects.attachments.serializers import BasicAttachmentsInfoSerializerMixin
from tuesmon.projects.due_dates.serializers import DueDateSerializerMixin
from tuesmon.projects.mixins.serializers import OwnerExtraInfoSerializerMixin
from tuesmon.projects.mixins.serializers import ProjectExtraInfoSerializerMixin
from tuesmon.projects.mixins.serializers import AssignedToExtraInfoSerializerMixin
from tuesmon.projects.mixins.serializers import StatusExtraInfoSerializerMixin
from tuesmon.projects.notifications.mixins import WatchedResourceSerializer
from tuesmon.projects.tagging.serializers import TaggedInProjectResourceSerializer
from tuesmon.projects.votes.mixins.serializers import VoteResourceSerializerMixin
from tuesmon.projects.history.mixins import TotalCommentsSerializerMixin


class TaskListSerializer(VoteResourceSerializerMixin, WatchedResourceSerializer,
                         OwnerExtraInfoSerializerMixin, AssignedToExtraInfoSerializerMixin,
                         StatusExtraInfoSerializerMixin, ProjectExtraInfoSerializerMixin,
                         BasicAttachmentsInfoSerializerMixin, TaggedInProjectResourceSerializer,
                         TotalCommentsSerializerMixin, DueDateSerializerMixin,
                         serializers.LightSerializer):

    id = Field()
    user_story = Field(attr="user_story_id")
    ref = Field()
    project = Field(attr="project_id")
    milestone = Field(attr="milestone_id")
    milestone_slug = MethodField()
    created_date = Field()
    modified_date = Field()
    finished_date = Field()
    subject = Field()
    us_order = Field()
    taskboard_order = Field()
    is_iocaine = Field()
    external_reference = Field()
    version = Field()
    watchers = Field()
    is_blocked = Field()
    blocked_note = Field()
    is_closed = MethodField()
    user_story_extra_info = Field()

    def get_generated_user_stories(self, obj):
        assert hasattr(obj, "generated_user_stories_attr"),\
            "instance must have a generated_user_stories_attr attribute"
        return obj.generated_user_stories_attr

    def get_milestone_slug(self, obj):
        return obj.milestone.slug if obj.milestone else None

    def get_is_closed(self, obj):
        return obj.status is not None and obj.status.is_closed


class TaskSerializer(TaskListSerializer):
    comment = MethodField()
    generated_user_stories = MethodField()
    blocked_note_html = MethodField()
    description = Field()
    description_html = MethodField()

    def get_comment(self, obj):
        return ""

    def get_blocked_note_html(self, obj):
        return mdrender(obj.project, obj.blocked_note)

    def get_description_html(self, obj):
        return mdrender(obj.project, obj.description)


class TaskNeighborsSerializer(NeighborsSerializerMixin, TaskSerializer):
    pass
