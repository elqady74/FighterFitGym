<<<<<<< HEAD
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # الصفحة الرئيسية
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),  # صفحة التسجيل
    path('api/', include('gym_app.urls')),  # مسارات الـ API
=======
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # الصفحة الرئيسية
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),  # صفحة التسجيل
    path('api/', include('gym_app.urls')),  # مسارات الـ API
>>>>>>> b60a3d5ebed84a802da2556ecaa12a22dfff3aea
]