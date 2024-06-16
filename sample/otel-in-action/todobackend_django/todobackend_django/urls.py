# urls.py

from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<str:toDo>', views.add_todo, name='add_todo'),  # Neue URL für das Hinzufügen von Todos
    path('todos/<str:pk>/', views.todo_detail, name='todo_detail'),
]
