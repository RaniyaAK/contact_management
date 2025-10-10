from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.user_logout, name='logout'),
    # path('dashboard/user/', views.user_dashboard, name='user_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact/<int:id>', views.contact, name='contact'),
    path('add_contacts/', views.add_contacts, name='add_contacts'),
    path('delete/<int:id>/', views.delete,name='delete'), 
    path('edit/<int:id>/',views.edit,name='edit'),
]
