from django.urls import path

from process import views

urlpatterns = [
    path('process/', views.SoundsView.as_view()),
]
