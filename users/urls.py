from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('signup/', views.SignUp.as_view()),
    path('test/', views.TestToken.as_view()),
]