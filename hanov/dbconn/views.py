from django.shortcuts import render, redirect
from .models import People
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PeopleSerializer
from django.db import IntegrityError


# Create your views here.

def db_index(request):
    site_users = People.objects.all()
    return render(request, 'dbconn/db_index.html', {'site_users': site_users})


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer



#
#
#
# class PeopleAPIList(generics.ListCreateAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
#
# class PeopleAPIUpdate(generics.UpdateAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
#
# class PeopleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer


# class PeopleAPIveiw(APIView):
#     def get(self):
#         userdata = People.objects.all()
#         return Response({'posts': PeopleSerializer(userdata, many=True).data})
#
#     def post(self, request):
#         serializer = PeopleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         try:
#             serializer.save()
#             return Response({'post': serializer.data})
#
#         except IntegrityError as e:
#             return Response({'Error:': str(e)})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Error": "Method PUT not allowed - PK invalid"})
#
#         try:
#             instance = People.objects.get(pk=pk)
#         except:
#             return Response({"Error": "Object doesn't exists"})
#
#         serializer = PeopleSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         try:
#             serializer.save()
#             return Response({'post': serializer.data})
#
#         except IntegrityError as e:
#             return Response({'Error:': str(e)})
#         # serializer.save()
# return Response({"posts": serializer.data})
