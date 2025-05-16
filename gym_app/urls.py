<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),  # API endpoint for signup
    path('login/', views.LoginView.as_view(), name='login'),  # API endpoint for login
=======
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),  # API endpoint for signup
    path('login/', views.LoginView.as_view(), name='login'),  # API endpoint for login
>>>>>>> b60a3d5ebed84a802da2556ecaa12a22dfff3aea
]