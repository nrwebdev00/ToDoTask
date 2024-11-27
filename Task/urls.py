from django.urls import path
from . import views

app_name = 'Task'

urlpatterns = [
    path('', views.list_view, name='task-list'),
    path('<int:id>', views.detail_view, name='task-detail'),
]