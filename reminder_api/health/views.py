from rest_framework.views import APIView
from rest_framework.response import Response

from project.models import Project, Environment
from reminder.models import Reminder, Stack, Host, Url

from rest_framework.response import Response

class HealthCheck(APIView):
    """
    View to display the health of the backend.
    """

    def get(self, request, format=None):
        """
        Return an overvew of the database content.
        """
        healthcheck = {
            'project_count': Project.objects.count(),
            'environment_count': Environment.objects.count(),
            'reminder_count': Reminder.objects.count(),
            'stack_count': Stack.objects.count(),
            'host_count': Host.objects.count(),
            'url_count': Url.objects.count()
        }
        return Response(healthcheck)
