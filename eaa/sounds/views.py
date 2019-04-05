from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sounds.models import Sound
from sounds.serializers import SoundSerializer

class SoundView(APIView):
    """
    Display the most recent sound
    """
    def get(self, pk):
        try:
            sound = Sound.objects.get(['time', 0])
            serializer = SoundSerializer(sound, many=False)
            return Response(serializer.data)
        except Sound.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SoundsView(APIView):
    """
    get:
        do something
    """
    def get(self, pk):
        try:
            sounds = Sound.objects.all()
            serializer = SoundSerializer(sounds, many=True)
            return Response(serializer.data)
        except Sound.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
