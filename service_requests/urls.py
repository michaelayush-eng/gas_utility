from django.urls import path
from . import views
app_name = 'service_requests'
urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('track/', views.track_request, name='track_request'),
    path('', views.home, name = 'home'),
    path('request_submitted/', views.request_submitted, name='request_submitted'),
]
