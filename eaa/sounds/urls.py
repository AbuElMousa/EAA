from django.urls import path

from sounds import views

urlpatterns = [
        path('sounds/', views.SoundsView.as_view()),
        path('sound/', views.SoundView.as_view()),
]
