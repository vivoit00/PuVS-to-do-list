from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

# views.py

@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all().values_list('todo', flat=True) 
        return Response(list(todos))
    
    #elif request.method == 'POST':
    #    serializer = TodoSerializer(data=request.data)
#
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_todo(request, toDo):
    # Neuen Todo-Eintrag erstellen
    serializer = TodoSerializer(data={'todo': toDo})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

