from rest_framework import serializers
from Process.models import Process

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('proc_id', 'option')