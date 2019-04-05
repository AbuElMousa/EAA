from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from configuration.models import Configuration
from configuration.serializers import ConfigurationSerializer

class ConfigurationView(APIView):
    """
    Display the current device configuration details
    """
    def get(self, pk):
        try:
            config = Configuration.objects.get(['config_id', 1])
            serializer = ConfigurationSerializer(config, many=False)
            return Response(serializer.data)
        except Configuration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = ConfigurationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
