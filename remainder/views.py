from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from remainder.forms import RegistrationForm,LoginForm,TodoCreateForm,TodoChangeForm
from django.views.generic import View,TemplateView,FormView,ListView,DetailView,UpdateView,CreateView
from django.contrib.auth import authenticate,login,logout
from remainder.models import Todos
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.query import QuerySet
from typing import Any
from django.forms.models import BaseModelForm
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class SignUpView(View):
    
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration completed successfully")
            return redirect("signin")
        else:
            messages.error(request,"faild to create account")
            return render(request,"signup.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"login failed")
                return render(request,"login.html",{"form":form})
            


@method_decorator(signin_required,name="dispatch")          
class IndexView(CreateView,ListView):
    # template_name="index.html"
    # def get(self,request,*args,**kwargs):
    #     form=TodoCreateForm()
    #     qs=Todos.objects.filter(user=request.user)
    #     return render(request,self.template_name,{"form":form,"todos":qs})
    
    template_name="index.html"
    form_class=TodoCreateForm
    context_object_name="todos"
    success_url=reverse_lazy("index")
    model=Todos
  

    # def post(self,request,*args,**kwargs):
    #     form=TodoCreateForm(request.POST)

    #     if form.is_valid():
    #         form.instance.user=request.user#to doo user login
    #         form.save()
    #         return redirect("index")
    #     else:
    #          return redirect("index")



    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        qs=Todos.objects.filter(user=self.request.user)
        return qs


    

@method_decorator(signin_required,name="dispatch") 
class TodoCreateView(FormView):
    template_name="remainder/todo_add.html"
    form_class=TodoCreateForm
    
    def post(self,request,*args,**kwargs):
        # if request.user.is_authenticated:
            form=TodoCreateForm(request.POST)
            if form.is_valid():
            # form.save()
                Todos.objects.create(**form.cleaned_data,user=request.user)
                messages.success(request,"Todos add sucessfully")
                return redirect("add-todo")

            else:
                messages.error(request,"failed")
                return render(request,self.template_name,{"form":form})
        # else:
        #     return redirect("signin")


@method_decorator(signin_required,name="dispatch")        
class TodoListView(ListView):
    template_name="remainder/todo_list.html"
    context_object_name="todos"
    model=Todos
    # models_name.objects.all()
    def get_queryset(self):
        qs=Todos.objects.filter(user=self.request.user)
        return qs

@method_decorator(signin_required,name="dispatch") 
class TodoDetailView(DetailView):


    template_name="remainder/todo_detail.html"
    context_object_name="todo"
    model=Todos


    # def get(self,request,*args,**kwrags):
    #     id=kwrags.get("pk")
    #     qs=Todos.objects.get(id=id)
    #     return render(request,self.template_name,{"todo":qs})
@method_decorator(signin_required,name="dispatch") 
class TodoUpdateView(UpdateView):



    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     obj=Todos.objects.get(id=id)
    #     form=TodoChangeForm(instance=obj)
    #     return render(request,self.template_name,{"form":form})

    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     obj=Todos.objects.get(id=id)
    #     form=TodoChangeForm(request.POST,instance=obj)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("list-todo")
    #     else:
    #         return render(request,self.template_name,{"form":form})
    
    template_name="remainder/todo_edit.html"
    form_class=TodoChangeForm
    model=Todos
    success_url=reverse_lazy("list-todo")

@signin_required
def remove_todo(request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).delete()
        print("deleted")
        return redirect("list-todo")


def SignOutView(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
