from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include

schema_view = get_swagger_view(title='SWAG')

urlpatterns = [
    url(r'^$', schema_view),
    path('', include('configuration.urls')),
    path('', include('sounds.urls')),
]
