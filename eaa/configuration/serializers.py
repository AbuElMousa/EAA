from rest_framework import serializers
from configuration.models import Configuration


'''
class ConfigurationSerializer(serializers.Serializer):
    config_id = serializers.IntegerField(read_only=True)
    target_frequencies = serializers.CharField(required=False)
    error_threshold = serializers.IntegerField(required=False)
    angle_offset = serializers.IntegerField(required=False)
    history = serializers.IntegerField(required=False)
    active_mics = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        Create and return a new configuration instance, given the validated data
        """
        return Configuration.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        return an existing configuration
        """
        instance.config_id = validated_data.get('config_id', instance.config_id)
        instance.target_frequencies = validated_data.get('target_frequencies', instance.target_frequencies)
        instance.error_threshold = validated_data.get('error_threshold', instance.error_threshold)
        instance.angle_offset = validated_data.get('angle_offset', instance.angle_offset)
        instance.history = validated_data.get('history', instance.history)
        instance.active_mics = validated_data.get('active_mics', instance.active_mics)
        return instance
'''

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('config_id', 'target_frequencies', 'error_threshold', 'angle_offset', 'history', 'active_mics')
