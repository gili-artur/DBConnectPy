from django.shortcuts import render, redirect
from .models import People
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PeopleSerializer
from django.db import IntegrityError
from rest_framework.exceptions import APIException


# Create your views here.

def db_index(request):
    site_users = People.objects.all
    return render(request, 'dbconn/db_index.html', {'site_users': site_users})


class PeopleAPIveiw(APIView):
    def get(self, request):
        userdata = People.objects.all()
        return Response({'posts': PeopleSerializer(userdata, many=True).data})

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            post_new = People.objects.create(
                surname=request.data['surname'],
                firstname=request.data['firstname'],
                patronymic=request.data['patronymic'],
                birthdate=request.data['birthdate'],
                city=request.data['city'],
                telephone=request.data['telephone'],
            )

            return Response({'post': PeopleSerializer(post_new).data})

        except IntegrityError as e:
            return Response({'Error:': str(e)})
