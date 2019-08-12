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
from django.utils.translation import ugettext as _

from tuesmon.base.api import serializers
from tuesmon.base.api import validators
from tuesmon.base.exceptions import ValidationError
from tuesmon.base.fields import PgArrayField
from tuesmon.projects.milestones.models import Milestone
from tuesmon.projects.mixins.validators import AssignedToValidator
from tuesmon.projects.notifications.mixins import EditableWatchedResourceSerializer
from tuesmon.projects.notifications.validators import WatchersValidator
from tuesmon.projects.tagging.fields import TagsAndTagsColorsField
from tuesmon.projects.validators import ProjectExistsValidator

from . import models


class IssueValidator(AssignedToValidator, WatchersValidator, EditableWatchedResourceSerializer,
                     validators.ModelValidator):

    tags = TagsAndTagsColorsField(default=[], required=False)
    external_reference = PgArrayField(required=False)

    class Meta:
        model = models.Issue
        read_only_fields = ('id', 'ref', 'created_date', 'modified_date', 'owner')


class IssuesBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    milestone_id = serializers.IntegerField(required=False)
    bulk_issues = serializers.CharField()


# Milestone bulk validators

class _IssueMilestoneBulkValidator(validators.Validator):
    issue_id = serializers.IntegerField()


class UpdateMilestoneBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    milestone_id = serializers.IntegerField()
    bulk_issues = _IssueMilestoneBulkValidator(many=True)

    def validate_milestone_id(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id": attrs[source]
        }
        if not Milestone.objects.filter(**filters).exists():
            raise ValidationError(_("The milestone isn't valid for the project"))
        return attrs

    def validate_bulk_tasks(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id__in": [issue["issue_id"] for issue in attrs[source]]
        }

        if models.Issue.objects.filter(**filters).count() != len(filters["id__in"]):
            raise ValidationError(_("All the issues must be from the same project"))

        return attrs
