import json
from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers

from .serializers import TodoSerializer
from .models import ToDo

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        mydata = json.loads(request.body)
        print(mydata)
        todo = ToDo.objects.create(title = mydata['title'], 
                                    description = mydata['description'], 
                                    author = request.user, 
                                    ) 
        serialized_obj = serializers.serialize('json', [todo, ]) 
        return HttpResponse(serialized_obj, content_type='application/json')
    
    
    def get_queryset(self , format=None): 
        todos = ToDo.objects.filter(author = self.request.user)
        #serializer = TodoSerializer(todos, many=True)
        return todos

