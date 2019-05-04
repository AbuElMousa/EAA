from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from voltages.models import Voltage
from voltages.serializers import VoltageSerializer

class VoltageView(APIView):
    """
    Display the most recent voltage
    """
    def get(self, pk):
        try:
            voltage = Voltages.objects.get(['volt_id', 1])
            serializer = VoltageSerializer(voltage, many=False)
            return Response(serializer.data)
        except Voltages.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)