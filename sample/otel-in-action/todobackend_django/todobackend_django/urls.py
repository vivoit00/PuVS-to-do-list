from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<str:pk>/', views.todo_detail, name='todo_detail_string'),
]

