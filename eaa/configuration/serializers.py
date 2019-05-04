from rest_framework import serializers
from configuration.models import Configuration

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('configId', 'targetFrequencies', 'errorThreshold', 'isDarkMode')
