from django.urls import path

from peaks import views

urlpatterns = [
    path('peaks/', views.SoundsView.as_view()),
]
