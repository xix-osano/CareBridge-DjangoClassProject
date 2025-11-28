from django.contrib import admin
from django.urls import path
from careapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('appointment/', views.Appoint, name='appointment'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('register/', views.register, name='register'),
    path('', views.login_user, name='login'),

]
