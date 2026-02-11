from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('report/', views.report_complaint, name='report'),
    path('status/', views.complaint_status, name='status'),
    path('awareness/', views.awareness, name='awareness'),

]
