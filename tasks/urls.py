from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/new/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:task_id>/send_invitation/', views.send_invitation_email, name='send_invitation'),
    path('admin/invite/', views.invite_user, name='admin_invite_user'),
]
