# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Tuesmon Agile LLC <support@tuesmon.com>
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

from tuesmon.base.api import viewsets
from tuesmon.base.decorators import list_route


class BaseImporterViewSet(viewsets.ViewSet):
    @list_route(methods=["GET"])
    def list_users(self, request, *args, **kwargs):
        raise NotImplementedError

    @list_route(methods=["GET"])
    def list_projects(self, request, *args, **kwargs):
        raise NotImplementedError

    @list_route(methods=["POST"])
    def import_project(self, request, *args, **kwargs):
        raise NotImplementedError

    @list_route(methods=["GET"])
    def auth_url(self, request, *args, **kwargs):
        raise NotImplementedError

    @list_route(methods=["POST"])
    def authorize(self, request, *args, **kwargs):
        raise NotImplementedError
