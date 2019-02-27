from django.urls import path

from configuration import views

urlpatterns = [
    path('configuration/', views.ConfigurationView.as_view())
]