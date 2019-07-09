from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    reported_at = serializers.CharField(max_length=30,require=False)
    avatar = serializers.ImageField(require=False)
    