

from django.contrib.auth.models import Group
from pastwatch_backend.users.models import User
from watcher.models import Data, Tag

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'type', 'created', 'modified', 'props')


class NestedTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'type', 'props')


class DataSerializer(serializers.ModelSerializer):
    tags = NestedTagSerializer(many=True, read_only=True)

    class Meta:
        model = Data
        fields = ('id', 'name', 'created', 'modified', 'tags', 'store')
