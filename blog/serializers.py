from abc import ABC

from rest_framework import serializers


class BlogBaseSerializer(serializers.Serializer):
    """
    data validation and serialization
    """
    title = serializers.CharField(allow_null=False)
    description = serializers.CharField(allow_null=False)
    summery = serializers.CharField()


class BlogCreateSerializer(BlogBaseSerializer):
    """
    data validation and serialization
    """
    category = serializers.CharField()


class BlogSerializer(BlogBaseSerializer):
    uid = serializers.CharField(allow_null=False)
    category = serializers.CharField()

