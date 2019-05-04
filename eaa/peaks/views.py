from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from peaks.models import Peak
from peaks.serializers import PeakSerializer

class peakView(APIView):
    """
    Display the most recent signal peak
    """
    def get(self, pk):
        try:
            peak = Peaks.objects.get(['peak_id', 1])
            serializer = PeakSerializer(peak, many=False)
            return Response(serializer.data)
        except Peaks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)