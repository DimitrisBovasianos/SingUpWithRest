# -*- coding: utf-8 -*-
from __future__ import unicode_literals
f
from .models import Tracker,MyUser
from django.http import HttpResponseRedirect,HttpRequest

from sirializers import UserSerializer
from rest_framework import generics,status,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class SingUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sing_up.html'

    def get(self,request):
        serializer = UserSerializer
        return Response({'serializer':serializer})

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return HttpResponseRedirect('/home')
