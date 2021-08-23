from abc import ABC

from rest_framework import serializers


class BlogBaseSerializer(serializers.Serializer):
    """
    This serialer is base that will be used in other serializer
    """
    title = serializers.CharField(allow_null=False)
    description = serializers.CharField(allow_null=False)
    summery = serializers.CharField()


class BlogCreateSerializer(BlogBaseSerializer):
    """
    This serialization class will be used for creating blog
    """
    category = serializers.CharField()


class BlogSerializer(BlogBaseSerializer):
    """
    This serialization class will be used for edit blog
    """

    uid = serializers.CharField(allow_null=False)
    category = serializers.CharField()

