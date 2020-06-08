from django.urls import path, include

from . import views

urlpatterns = [
    # just dashboard
    path('', views.dashboard, name='dashboard'),
    # Authentication
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # Social media authentication
    path('', include('social_django.urls', namespace='social')),
]
