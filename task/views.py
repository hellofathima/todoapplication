from django.shortcuts import render,redirect
from django.views.generic import View
from task.forms import TodoCreateForm,TodoChangeForm
from task.models import Todos
from rest_framework.viewsets import ViewSet

# Create your views here.
class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TodoCreateForm()#create an instance of Todocreateform

        return render(request,"todo_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        
        # form=TodoCreateForm(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)
        #     Todos.objects.create(**form.cleaned_data)
            
        #     print("To dos created")
        #     return render(request,"todo_add.html",{"form":form})
            

        # else:
        #     return render(request,"todo_add.html",{"form":form})
        form=TodoCreateForm(request.POST)  

        if form.is_valid():
            form.save()
            return redirect("todo-list")
        else:
            return render(request,"todo_add.html",{"form":form})

        
class TodoListView(View):
    def get(self,request,*args,**kwargs):
        
        qs=Todos.objects.all()
        return render(request,"todo_list.html",{"todos":qs})
    

class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        print("inside detail view")
        id=kwargs.get("pk")
        print(kwargs)
        qs=Todos.objects.get(id=id)
        return render(request,"todo_detail.html",{"todos":qs})
    

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).delete()
        return redirect("todo-list")

class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)
        form=TodoChangeForm(instance=obj)
        return render(request,"todo_edit.html",{"form":form})
        
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)

        form=TodoChangeForm(request.POST,instance=obj)

        if form.is_valid():

             form.save()
             return redirect("todo-list")
        else:
            return render(request,"todo_edit.html",{"form":form})
