from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from todo.models import Todo

# Create your views here.
class TodoAPIView(APIView):
    @staticmethod 
    def get(request, *args, **kwargs):
        todos = Todo.objects.all()
        rs = []
        for todo in todos:
            rs.append(model_to_dict(todo))
        return Response(rs,status=status.HTTP_200_OK)
    
    @staticmethod 
    def post(request, *args, **kwargs):
        data = Todo.objects.create(
            title=request.data.get("title", None),
            description=request.data.get("description", None),
        )
        return Response(model_to_dict(data),status=status.HTTP_201_CREATED)
    
    @staticmethod 
    def patch(request, *args, **kwargs):
        id = request.data.get("id", None)
        todo = Todo.objects.filter(pk=id).first()
        if not todo:
            return Response({"status": f'{id}: not found!'},status=status.HTTP_404_NOT_FOUND)
        if request.data.get("title", None):
            todo.title = request.data.get("title", None)
        if request.data.get("description", None):
            todo.description = request.data.get("description", None)
        if request.data.get("done", None):
            todo.done = request.data.get("done", None)
        todo.save()
        return Response(model_to_dict(todo),status=status.HTTP_200_OK)
    

class TodoWithIDAPIView(APIView):
    @staticmethod 
    def get(request, *args, **kwargs):
        id = kwargs.get("id", None)
        todo = Todo.objects.filter(pk=id).first()
        if not todo:
            return Response({"status": f'{id}: not found!'},status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(todo),status=status.HTTP_200_OK)
    
    @staticmethod 
    def delete(request, *args, **kwargs):
        id = kwargs.get("id", None)
        todo = Todo.objects.filter(pk=id).first()
        if not todo:
            return Response({"status": f'{id}: not found!'},status=status.HTTP_404_NOT_FOUND)
        title = todo.title
        todo.delete()
        return Response({"status": f'{id}: {title} deleted!'},status=status.HTTP_200_OK)