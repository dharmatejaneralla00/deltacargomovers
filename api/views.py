from django.apps import apps
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers

clientlist = apps.get_model('login','clientlist')
# Create your views here.
class ClientlistView(APIView):

    def get(self,r,name):
        return Response({"status":True,"data":serializers.ClientSerializer(clientlist.objects.get(clientname = name)).data},status=200)