from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from configuration.models import Configuration
from configuration.serializers import ConfigurationSerializer

class ConfigurationView(APIView):
    """
    Display the current device configuration details
    """
    def get(self, request, format=None):
        #serializer = ConfigurationSerializer(request)
        import random
        return Response({"mode": random.random()})