from django.urls import path

from .views import TodoListViewSet, TaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('todos', TodoListViewSet, basename='todo')

urlpatterns = [
    # path('todos/', TodoListViewSet.as_view({'get': 'list'}), name='all_lists_show')
    # path('todos/<int:list_id>/', TodoListViewSet.as_view({'get': 'retrieve'}), name="whole_list_show"),
    # path('todos/<int:list_id>/uncompleted/', TodoListViewSet.as_view({'get': 'retrieve_incomplete'}), name="completed_list_show"),
    # path('todos/<int:list_id>/completed/', TodoListViewSet.as_view({'get': 'retrieve_complete'}), name="completed_list_show"),
    # path('tasks/', TaskViewSet.as_view(), name='tasks'),
]

urlpatterns += router.urls