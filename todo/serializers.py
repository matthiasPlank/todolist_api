from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import ToDo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at']

