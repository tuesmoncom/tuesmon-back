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

from tuesmon.base import routers
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)

# Locales
from tuesmon.locale.api import LocalesViewSet

router.register(r"locales", LocalesViewSet, base_name="locales")


# Users & Roles
from tuesmon.auth.api import AuthViewSet
from tuesmon.users.api import UsersViewSet
from tuesmon.users.api import RolesViewSet

router.register(r"auth", AuthViewSet, base_name="auth")
router.register(r"users", UsersViewSet, base_name="users")
router.register(r"roles", RolesViewSet, base_name="roles")


# User Storage
from tuesmon.userstorage.api import StorageEntriesViewSet

router.register(r"user-storage", StorageEntriesViewSet, base_name="user-storage")


# Notifications & Notify policies
from tuesmon.projects.notifications.api import NotifyPolicyViewSet
from tuesmon.projects.notifications.api import WebNotificationsViewSet

router.register(r"notify-policies", NotifyPolicyViewSet, base_name="notifications")
router.register(r"web-notifications", WebNotificationsViewSet, base_name="web-notifications")
router.register(r"web-notifications/set-as-read", WebNotificationsViewSet, base_name="web-notifications")
router.register(r"web-notifications/(?P<resource_id>\d+)/set-as-read", WebNotificationsViewSet, base_name="web-notifications")

# Project settings
from tuesmon.projects.settings.api import UserProjectSettingsViewSet, SectionsViewSet

router.register(r"user-project-settings", UserProjectSettingsViewSet, base_name="user-project-settings")
router.register(r"sections", SectionsViewSet, base_name="sections")


# Projects & Selectors
from tuesmon.projects.api import ProjectViewSet
from tuesmon.projects.api import ProjectFansViewSet
from tuesmon.projects.api import ProjectWatchersViewSet
from tuesmon.projects.api import MembershipViewSet
from tuesmon.projects.api import InvitationViewSet
from tuesmon.projects.api import EpicStatusViewSet
from tuesmon.projects.api import UserStoryStatusViewSet
from tuesmon.projects.api import PointsViewSet
from tuesmon.projects.api import UserStoryDueDateViewSet
from tuesmon.projects.api import TaskStatusViewSet
from tuesmon.projects.api import TaskDueDateViewSet
from tuesmon.projects.api import IssueStatusViewSet
from tuesmon.projects.api import IssueTypeViewSet
from tuesmon.projects.api import IssueDueDateViewSet
from tuesmon.projects.api import PriorityViewSet
from tuesmon.projects.api import SeverityViewSet
from tuesmon.projects.api import ProjectTemplateViewSet

router.register(r"projects", ProjectViewSet, base_name="projects")
router.register(r"projects/(?P<resource_id>\d+)/fans", ProjectFansViewSet, base_name="project-fans")
router.register(r"projects/(?P<resource_id>\d+)/watchers", ProjectWatchersViewSet, base_name="project-watchers")
router.register(r"project-templates", ProjectTemplateViewSet, base_name="project-templates")
router.register(r"memberships", MembershipViewSet, base_name="memberships")
router.register(r"invitations", InvitationViewSet, base_name="invitations")
router.register(r"epic-statuses", EpicStatusViewSet, base_name="epic-statuses")
router.register(r"userstory-statuses", UserStoryStatusViewSet, base_name="userstory-statuses")
router.register(r"points", PointsViewSet, base_name="points")
router.register(r"userstory-due-dates", UserStoryDueDateViewSet, base_name="userstory-due-dates")
router.register(r"task-statuses", TaskStatusViewSet, base_name="task-statuses")
router.register(r"task-due-dates", TaskDueDateViewSet, base_name="task-due-dates")
router.register(r"issue-statuses", IssueStatusViewSet, base_name="issue-statuses")
router.register(r"issue-types", IssueTypeViewSet, base_name="issue-types")
router.register(r"issue-due-dates", IssueDueDateViewSet, base_name="issue-due-dates")
router.register(r"priorities", PriorityViewSet, base_name="priorities")
router.register(r"severities",SeverityViewSet , base_name="severities")


# Custom Attributes
from tuesmon.projects.custom_attributes.api import EpicCustomAttributeViewSet
from tuesmon.projects.custom_attributes.api import UserStoryCustomAttributeViewSet
from tuesmon.projects.custom_attributes.api import TaskCustomAttributeViewSet
from tuesmon.projects.custom_attributes.api import IssueCustomAttributeViewSet

from tuesmon.projects.custom_attributes.api import EpicCustomAttributesValuesViewSet
from tuesmon.projects.custom_attributes.api import UserStoryCustomAttributesValuesViewSet
from tuesmon.projects.custom_attributes.api import TaskCustomAttributesValuesViewSet
from tuesmon.projects.custom_attributes.api import IssueCustomAttributesValuesViewSet

router.register(r"epic-custom-attributes", EpicCustomAttributeViewSet,
                base_name="epic-custom-attributes")
router.register(r"userstory-custom-attributes", UserStoryCustomAttributeViewSet,
                base_name="userstory-custom-attributes")
router.register(r"task-custom-attributes", TaskCustomAttributeViewSet,
                base_name="task-custom-attributes")
router.register(r"issue-custom-attributes", IssueCustomAttributeViewSet,
                base_name="issue-custom-attributes")

router.register(r"epics/custom-attributes-values", EpicCustomAttributesValuesViewSet,
                base_name="epic-custom-attributes-values")
router.register(r"userstories/custom-attributes-values", UserStoryCustomAttributesValuesViewSet,
                base_name="userstory-custom-attributes-values")
router.register(r"tasks/custom-attributes-values", TaskCustomAttributesValuesViewSet,
                base_name="task-custom-attributes-values")
router.register(r"issues/custom-attributes-values", IssueCustomAttributesValuesViewSet,
                base_name="issue-custom-attributes-values")


# Search
from tuesmon.searches.api import SearchViewSet

router.register(r"search", SearchViewSet, base_name="search")


# Resolver
from tuesmon.projects.references.api import ResolverViewSet

router.register(r"resolver", ResolverViewSet, base_name="resolver")


# Attachments
from tuesmon.projects.attachments.api import EpicAttachmentViewSet
from tuesmon.projects.attachments.api import UserStoryAttachmentViewSet
from tuesmon.projects.attachments.api import IssueAttachmentViewSet
from tuesmon.projects.attachments.api import TaskAttachmentViewSet
from tuesmon.projects.attachments.api import WikiAttachmentViewSet

router.register(r"epics/attachments", EpicAttachmentViewSet,
                base_name="epic-attachments")
router.register(r"userstories/attachments", UserStoryAttachmentViewSet,
                base_name="userstory-attachments")
router.register(r"tasks/attachments", TaskAttachmentViewSet,
                base_name="task-attachments")
router.register(r"issues/attachments", IssueAttachmentViewSet,
                base_name="issue-attachments")
router.register(r"wiki/attachments", WikiAttachmentViewSet,
                base_name="wiki-attachments")


# Project components
from tuesmon.projects.milestones.api import MilestoneViewSet
from tuesmon.projects.milestones.api import MilestoneWatchersViewSet

from tuesmon.projects.epics.api import EpicViewSet
from tuesmon.projects.epics.api import EpicRelatedUserStoryViewSet
from tuesmon.projects.epics.api import EpicVotersViewSet
from tuesmon.projects.epics.api import EpicWatchersViewSet

from tuesmon.projects.userstories.api import UserStoryViewSet
from tuesmon.projects.userstories.api import UserStoryVotersViewSet
from tuesmon.projects.userstories.api import UserStoryWatchersViewSet

from tuesmon.projects.tasks.api import TaskViewSet
from tuesmon.projects.tasks.api import TaskVotersViewSet
from tuesmon.projects.tasks.api import TaskWatchersViewSet

from tuesmon.projects.issues.api import IssueViewSet
from tuesmon.projects.issues.api import IssueVotersViewSet
from tuesmon.projects.issues.api import IssueWatchersViewSet

from tuesmon.projects.wiki.api import WikiViewSet
from tuesmon.projects.wiki.api import WikiLinkViewSet
from tuesmon.projects.wiki.api import WikiWatchersViewSet

router.register(r"milestones", MilestoneViewSet,
                base_name="milestones")
router.register(r"milestones/(?P<resource_id>\d+)/watchers", MilestoneWatchersViewSet,
                base_name="milestone-watchers")

router.register(r"epics", EpicViewSet, base_name="epics")\
      .register(r"related_userstories", EpicRelatedUserStoryViewSet,
                base_name="epics-related-userstories",
                parents_query_lookups=["epic"])

router.register(r"epics/(?P<resource_id>\d+)/voters", EpicVotersViewSet,
                base_name="epic-voters")
router.register(r"epics/(?P<resource_id>\d+)/watchers", EpicWatchersViewSet,
                base_name="epic-watchers")

router.register(r"userstories", UserStoryViewSet,
                base_name="userstories")
router.register(r"userstories/(?P<resource_id>\d+)/voters", UserStoryVotersViewSet,
                base_name="userstory-voters")
router.register(r"userstories/(?P<resource_id>\d+)/watchers", UserStoryWatchersViewSet,
                base_name="userstory-watchers")

router.register(r"tasks", TaskViewSet,
                base_name="tasks")
router.register(r"tasks/(?P<resource_id>\d+)/voters", TaskVotersViewSet,
                base_name="task-voters")
router.register(r"tasks/(?P<resource_id>\d+)/watchers", TaskWatchersViewSet,
                base_name="task-watchers")

router.register(r"issues", IssueViewSet,
                base_name="issues")
router.register(r"issues/(?P<resource_id>\d+)/voters", IssueVotersViewSet,
                base_name="issue-voters")
router.register(r"issues/(?P<resource_id>\d+)/watchers", IssueWatchersViewSet,
                base_name="issue-watchers")

router.register(r"wiki", WikiViewSet,
                base_name="wiki")
router.register(r"wiki/(?P<resource_id>\d+)/watchers", WikiWatchersViewSet,
                base_name="wiki-watchers")
router.register(r"wiki-links", WikiLinkViewSet,
                base_name="wiki-links")


# Delete owned projects
from tuesmon.projects.api import DeleteOwnProjectsViewSet

router.register(r"delete-owned-projects", DeleteOwnProjectsViewSet,
                base_name="delete-owned-projects")


# History & Components
from tuesmon.projects.history.api import EpicHistory
from tuesmon.projects.history.api import UserStoryHistory
from tuesmon.projects.history.api import TaskHistory
from tuesmon.projects.history.api import IssueHistory
from tuesmon.projects.history.api import WikiHistory

router.register(r"history/epic", EpicHistory, base_name="epic-history")
router.register(r"history/userstory", UserStoryHistory, base_name="userstory-history")
router.register(r"history/task", TaskHistory, base_name="task-history")
router.register(r"history/issue", IssueHistory, base_name="issue-history")
router.register(r"history/wiki", WikiHistory, base_name="wiki-history")

# Contact
from tuesmon.projects.contact.api import ContactViewSet
router.register(r"contact", ContactViewSet, base_name="contact")


# Timelines
from tuesmon.timeline.api import ProfileTimeline
from tuesmon.timeline.api import UserTimeline
from tuesmon.timeline.api import ProjectTimeline

router.register(r"timeline/profile", ProfileTimeline, base_name="profile-timeline")
router.register(r"timeline/user", UserTimeline, base_name="user-timeline")
router.register(r"timeline/project", ProjectTimeline, base_name="project-timeline")


# Webhooks
from tuesmon.webhooks.api import WebhookViewSet
from tuesmon.webhooks.api import WebhookLogViewSet

router.register(r"webhooks", WebhookViewSet, base_name="webhooks")
router.register(r"webhooklogs", WebhookLogViewSet, base_name="webhooklogs")


# GitHub webhooks
from tuesmon.hooks.github.api import GitHubViewSet

router.register(r"github-hook", GitHubViewSet, base_name="github-hook")


# Gitlab webhooks
from tuesmon.hooks.gitlab.api import GitLabViewSet

router.register(r"gitlab-hook", GitLabViewSet, base_name="gitlab-hook")


# Bitbucket webhooks
from tuesmon.hooks.bitbucket.api import BitBucketViewSet

router.register(r"bitbucket-hook", BitBucketViewSet, base_name="bitbucket-hook")


# Gogs webhooks
from tuesmon.hooks.gogs.api import GogsViewSet

router.register(r"gogs-hook", GogsViewSet, base_name="gogs-hook")


# Importer
from tuesmon.export_import.api import ProjectImporterViewSet, ProjectExporterViewSet

router.register(r"importer", ProjectImporterViewSet, base_name="importer")
router.register(r"exporter", ProjectExporterViewSet, base_name="exporter")


# External apps
from tuesmon.external_apps.api import Application, ApplicationToken

router.register(r"applications", Application, base_name="applications")
router.register(r"application-tokens", ApplicationToken, base_name="application-tokens")

# Third party importers
if settings.IMPORTERS.get('trello', {}).get('active', False):
    from tuesmon.importers.trello.api import TrelloImporterViewSet
    router.register(r"importers/trello", TrelloImporterViewSet, base_name="importers-trello")

if settings.IMPORTERS.get('jira', {}).get('active', False):
    from tuesmon.importers.jira.api import JiraImporterViewSet
    router.register(r"importers/jira", JiraImporterViewSet, base_name="importers-jira")

if settings.IMPORTERS.get('github', {}).get('active', False):
    from tuesmon.importers.github.api import GithubImporterViewSet
    router.register(r"importers/github", GithubImporterViewSet, base_name="importers-github")

if settings.IMPORTERS.get('asana', {}).get('active', False):
    from tuesmon.importers.asana.api import AsanaImporterViewSet
    router.register(r"importers/asana", AsanaImporterViewSet, base_name="importers-asana")


# Stats
#   - see tuesmon.stats.routers and tuesmon.stats.apps


# Feedback
#   - see tuesmon.feedback.routers and tuesmon.feedback.apps
