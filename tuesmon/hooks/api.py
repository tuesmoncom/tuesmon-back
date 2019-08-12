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

from tuesmon.base import exceptions as exc
from tuesmon.base import response
from tuesmon.base.api.viewsets import GenericViewSet
from tuesmon.base.utils import json
from tuesmon.projects.models import Project

from .exceptions import ActionSyntaxException


class BaseWebhookApiViewSet(GenericViewSet):
    # We don't want rest framework to parse the request body and transform it in
    # a dict in request.DATA, we need it raw
    parser_classes = ()

    # This dict associates the event names we are listening for
    # with their reponsible classes (extending event_hooks.BaseEventHook)
    event_hook_classes = {}

    def _validate_signature(self, project, request):
        raise NotImplemented

    def _get_project(self, request):
        project_id = request.GET.get("project", None)
        try:
            project = Project.objects.get(id=project_id)
            return project
        except (ValueError, Project.DoesNotExist):
            return None

    def _get_payload(self, request):
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except ValueError:
            raise exc.BadRequest(_("The payload is not a valid json"))
        return payload

    def _get_event_name(self, request):
        raise NotImplemented

    def create(self, request, *args, **kwargs):
        project = self._get_project(request)
        if not project:
            raise exc.BadRequest(_("The project doesn't exist"))

        if not self._validate_signature(project, request):
            raise exc.BadRequest(_("Bad signature"))

        if project.blocked_code is not None:
            raise exc.Blocked(_("Blocked element"))

        event_name = self._get_event_name(request)

        payload = self._get_payload(request)

        event_hook_class = self.event_hook_classes.get(event_name, None)
        if event_hook_class is not None:
            event_hook = event_hook_class(project, payload)
            try:
                event_hook.process_event()
            except ActionSyntaxException as e:
                raise exc.BadRequest(e)

        return response.NoContent()
