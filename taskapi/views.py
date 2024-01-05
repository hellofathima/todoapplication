from django.shortcuts import render

# Create your views here.

#using Viewset
from task.models import Todos
from rest_framework.response  import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from taskapi.serializers import TodoSerializer
from rest_framework.decorators import action

# class TodoViewsetView(ViewSet):
#     def list(self,request,*args,**kwargs):

#             qs=Todos.objects.all()
#             serializer=TodoSerializer(qs,many=True) #deserializer
#             return Response(data=serializer.data)
    
#     def retrieve(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         qs=Todos.objects.get(id=id)
#         serializer=TodoSerializer(qs)
#         return Response(data=serializer.data)

    
#     def create(self,request,*args,**kwargs):
#         serializer=TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)

#     def update(self,request,*args,**kwargs):

#         id=kwargs.get("pk")
#         obj=Todos.objects.get(id=id)
#         serializer=TodoSerializer(data=request.data,instance=obj)#update obj with this data
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     def destroy(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         Todos.objects.filter(id=id).delete()
        
#         return Response(data={"message":"deleted"})
class TodoViewsetView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()

#custom method can be defined and decorated by decortr mention method and details
    @action(methods=["get"],detail=False)
    #localhost:8000/api/todos/completed/
    #details= if hav id then true else false
    def completed(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=True)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
    

    #localhost:8000/api/todos/pending/
    @action(methods=["get"],detail=False)
    def pending(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=False)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)