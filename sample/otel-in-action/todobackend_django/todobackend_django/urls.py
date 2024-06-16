from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<str:toDo>', views.modify_todo, name='modify_todo'),  
]
