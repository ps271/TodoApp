from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


# Create your views here.

@api_view(['GET'])
def OverView(request):
    api_urls = {
        'List' : '/task-list',
        'Detail View' : '/task-detail/<str:pk>',
        'Create' : '/task-create',
        'Delete' : '/task-delete/<str:pk>',
        'Update' : '/task-update/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    data = request.data
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return ('Error Occured')

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return ('Item Deleted Successfully')

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return ('Some Error Occured')


