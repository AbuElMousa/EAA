from rest_framework import serializers
from Peak.models import Peak

class PeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ('peak_id', 'top_left', 'bottom_left')