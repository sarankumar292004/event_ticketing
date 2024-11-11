from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.create_event, name='create_event'),
    path('event/<int:pk>/book/', views.book_ticket, name='book_ticket'),
]
