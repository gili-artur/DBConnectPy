from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

from dbconn.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', PeopleViewSet)

# https://django-rest-swagger.readthedocs.io/en/latest/
schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('db/', include('dbconn.urls')),
                  path('api/', include(router.urls)),
                  path('api/doc', schema_view)

                  # path('api/', PeopleViewSet.as_view({'get': 'list'})),
                  # path('api/<int:pk>/', PeopleViewSet.as_view({'put': 'update'})),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
