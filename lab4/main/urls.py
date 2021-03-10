from django.urls import path

from . import views

urlpatterns = [
    path('<int:list_id>/', views.uncompleted_list_show, name="uncompleted_list_show"),
    path('<int:list_id>/completed/', views.completed_list_show, name="completed_list_show")
]