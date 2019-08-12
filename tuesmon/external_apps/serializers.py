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
from tuesmon.base.fields import Field

from . import models
from . import services

from django.utils.translation import ugettext as _


class ApplicationSerializer(serializers.LightSerializer):
    id = Field()
    name = Field()
    web = Field()
    description = Field()
    icon_url = Field()


class ApplicationTokenSerializer(serializers.LightSerializer):
    id = Field()
    user = Field(attr="user_id")
    application = ApplicationSerializer()
    auth_code = Field()
    next_url = Field()


class AuthorizationCodeSerializer(serializers.LightSerializer):
    state = Field()
    auth_code = Field()
    next_url = Field()


class AccessTokenSerializer(serializers.LightSerializer):
    token = Field()
