from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('complaints/', views.admin_complaints, name='admin_complaints'),
    path('update/<int:id>/', views.update_complaint, name='update_complaint'),
    path('awareness/', views.admin_awareness, name='admin_awareness'),

]
