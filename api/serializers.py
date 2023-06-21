from rest_framework import serializers

class JsonSearchSerializer(serializers.Serializer):
    query = serializers.JSONField()

class IdentifierRangeSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    range = serializers.IntegerField()