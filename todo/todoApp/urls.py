from django.urls import path
from . import views

app_name = 'todoApp'

urlpatterns = [
    path('', views.OverView, name='api-overview'),
    path('task-list', views.taskList, name='list-view'),
    path('task-detail/<str:pk>', views.taskDetail, name='detail-view'),
    path('task-create', views.taskCreate, name='create-view'),
    path('task-delete/<str:pk>', views.taskDelete, name='delete-view'),
    path('task-update/<str:pk>', views.taskUpdate, name='update-view'),

]