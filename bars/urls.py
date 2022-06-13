from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bars),
    path('bar/<int:pk>/', views.get_bar)
]