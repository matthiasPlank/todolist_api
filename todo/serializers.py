from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import ToDo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'first_name' , 'last_name' , 'username' , 'email']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at' , 'author' , 'time_passed']

