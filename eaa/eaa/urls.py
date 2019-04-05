from django.urls import path, include

urlpatterns = [
    path('', include('configuration.urls')),
    path('', include('sounds.urls')),
]
