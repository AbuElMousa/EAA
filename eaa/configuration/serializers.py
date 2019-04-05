from rest_framework import serializers
from configuration.models import Configuration

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('config_id', 'target_frequencies', 'error_threshold', 'angle_offset', 'history', 'active_mics')
