from django.apps import apps
from rest_framework import serializers

clientlist = apps.get_model('login','clientlist')

class ClientSerializer(serializers.ModelSerializer):
    clientname = serializers.CharField(max_length=30)
    fromadd = serializers.CharField(max_length=100)
    fname = serializers.CharField(max_length=100)
    fno = serializers.IntegerField()
    usercode = serializers.CharField(max_length=10)

    class Meta:
        model = clientlist
        fields = '__all__'