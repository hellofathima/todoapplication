from django import forms
from task.models import Todos

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields={"title","user","due_date","status"}
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"}),
            "due_date":forms.DateTimeInput(attrs={"type":"date","style":"color:red;"}),
            
        }


# class TodoCreateForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     user=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     due_date=forms.DateField(widget=forms.DateTimeInput(attrs={"type":"date","style":"color:red;"}))
    
# class TodoChangeForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date","style":"color:red;"}))
#     status=forms.BooleanField()

class TodoChangeForm(forms.ModelForm):

    class Meta:
        model=Todos
        fields=["title","due_date","status"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            
            "due_date":forms.DateInput(attrs={"type":"date","style":"color:red;"})}
            
        
                

