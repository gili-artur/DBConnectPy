from django.urls import path
from . import views
from .views import PeopleAPIveiw

urlpatterns = [
    path('', views.db_index, name='dbase'),
    # path('api/', PeopleAPIveiw.as_view()),
]
