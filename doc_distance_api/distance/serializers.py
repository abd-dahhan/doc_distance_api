from rest_framework import serializers


class StatsSerializer(serializers.Serializer):
    text = serializers.CharField()
    response = serializers.ListField(read_only=True)


class WordFreqSerializer(serializers.Serializer):
    payload = serializers.ListField()


class SimilaritySerializer(serializers.Serializer):
    payload1 = serializers.ListField()
    payload2 = serializers.ListField()





