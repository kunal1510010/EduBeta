from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('data/<str:file_name>/', views.data, name='data'),
]
