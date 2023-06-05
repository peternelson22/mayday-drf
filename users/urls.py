
from django.urls import path
from . import views

urlpatterns = [
path('signup/', views.SignUp.as_view()),
path('login/', views.Login.as_view()),

]
