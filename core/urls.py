
from .views import *
from django.urls import path

urlpatterns = [
    path('', Home.as_view()),
    path('<int:pk>/', HomeDetails.as_view()),
]
