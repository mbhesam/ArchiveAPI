from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    query = serializers.JSONField()
