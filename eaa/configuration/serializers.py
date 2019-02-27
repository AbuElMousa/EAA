from rest_framework import serializers

from configuration.models import Configuration

'''class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('mode',)'''

class ConfigurationSerializer(serializers.Serializer):
    mode = serializers.IntegerField()
    def update(self, instance, validated_data):
        """
        return an existing configuration
        """
        instance.mode = 3
        return instance