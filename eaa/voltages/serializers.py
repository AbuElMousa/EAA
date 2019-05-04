from rest_framework import serializers
from vltages.models import Voltage

class VoltageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voltage
        fields = ('volt_id', 'top_left', 'bottom_left')