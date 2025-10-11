from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    
    path('contacts/', views.contacts, name='contacts'),
    path('add_contacts/', views.add_contacts, name='add_contacts'),
    path('delete/<int:id>/', views.delete,name='delete'), 
    path('edit/<int:id>/',views.edit,name='edit'),

    path('manage_contacts/', views.manage_contacts, name='manage_contacts'),
    path('manage_contacts/edit/<int:id>/', views.manage_contacts_edit, name='manage_contacts_edit'),
    path('manage_contacts/delete/<int:id>/', views.manage_contacts_delete, name='manage_contacts_delete'),

    path('manage_users/', views.manage_users, name='manage_users'),
    path('manage_users_delete/<int:id>/', views.manage_users_delete, name='manage_users_delete'),
    path('manage_users_edit/<int:id>/', views.manage_users_edit, name='manage_users_edit'),


]


