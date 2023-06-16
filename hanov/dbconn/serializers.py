from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


class PeopleSerializer(serializers.Serializer):
    surname = serializers.CharField()
    firstname = serializers.CharField()
    patronymic = serializers.CharField()
    birthdate = serializers.DateField()
    city = serializers.CharField()
    telephone = serializers.CharField(max_length=11)
