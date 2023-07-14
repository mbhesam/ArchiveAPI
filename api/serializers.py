from rest_framework import serializers

class JsonSearchSerializer(serializers.Serializer):
    query = serializers.JSONField()

class IdentifierRangeSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    range = serializers.IntegerField()

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class UpdateSerializer(serializers.Serializer):
    find_query = serializers.JSONField()
    update_query = serializers.JSONField()