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
from tuesmon.base.api import validators

from . import models


class AttachmentValidator(validators.ModelValidator):
    attached_file = serializers.FileField(required=True)

    class Meta:
        model = models.Attachment
        fields = ("id", "project", "owner", "name", "attached_file", "size",
                  "description", "is_deprecated", "created_date",
                  "modified_date", "object_id", "order", "sha1", "from_comment")
        read_only_fields = ("owner", "created_date", "modified_date", "sha1")
