from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from process.models import Process
from process.serializers import ProcessSerializer

class ProcessView(APIView):
    """
    post if a restart is needed
    """

    def post(self, request, format=None):
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
