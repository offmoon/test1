from django.urls import path

from . import views

urlpatterns = [
    path('',views.hello),
    path('2/', views.hello2),
]