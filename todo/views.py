import json
from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers

from .serializers import TodoSerializer
from .models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated


    def create(self, request):
        mydata = json.loads(request.body)
        print(mydata)
        todo = ToDo.objects.create(title = mydata['title'], 
                                    description = mydata['description'], 
                                    author = request.user, 
                                    ) 
        serialized_obj = serializers.serialize('json', [todo, ]) 
        return HttpResponse(serialized_obj, content_type='application/json')

