from django.urls import path

from voltages import views

urlpatterns = [
    path('voltages/', views.SoundsView.as_view()),
]
