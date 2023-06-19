from django.shortcuts import render, redirect
from .models import People
from rest_framework import viewsets
from .serializers import PeopleSerializer


# Create your views here.

def db_index(request):
    site_users = People.objects.all()
    return render(request, 'dbconn/db_index.html', {'site_users': site_users})


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


