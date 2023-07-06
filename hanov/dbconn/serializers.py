from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

# class PeopleSerializer(serializers.Serializer):
#     surname = serializers.CharField()
#     firstname = serializers.CharField()
#     patronymic = serializers.CharField()
#     birthdate = serializers.DateField()
#     city = serializers.CharField()
#     telephone = serializers.CharField(max_length=11)

# class PeopleSerializer(serializers.Serializer):
#     surname = serializers.CharField()
#     firstname = serializers.CharField()
#     patronymic = serializers.CharField()
#     birthdate = serializers.DateField()
#     city = serializers.CharField()
#     telephone = serializers.CharField(max_length=11)
#
#     def create(self, validated_data):
#         return People.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.surname = validated_data.get("surname", instance.surname)
#         instance.firstname = validated_data.get("firstname", instance.firstname)
#         instance.patronymic = validated_data.get("patronymic", instance.patronymic)
#         instance.birthdate = validated_data.get("birthdate", instance.birthdate)
#         instance.city = validated_data.get("city", instance.city)
#         instance.telephone = validated_data.get("telephone", instance.telephone)
#         instance.save()
#         return instance
