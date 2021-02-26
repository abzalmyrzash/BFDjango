from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.uncompleted_list_show),
    path('todos/completed', views.completed_list_show)
]