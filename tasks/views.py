from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.
class NewTaskForm(forms.Form):
   tasks=forms.CharField(label="New Task ") 
#    pritoriy=forms.IntegerField(label="Priority",min_value=1,max_value=5)

def index(request):
    if "tasks" not in request.session: 
        request.session["tasks"]=[]
    return render(request,"tasks/index.html",{
           "tasks":  request.session["tasks"]
       
    })
def add(request):
    if request.method=="POST":
         form=NewTaskForm(request.POST)
         if form.is_valid():
             tasks=form.cleaned_data["tasks"]
             request.session["tasks"]+[tasks]
             return HttpResponseRedirect(reverse("tasks:index"))
         else:
             return render(request, "tasks/add.html",{
                 "form" :form
             })    


    return render(request,"tasks/add.html",{
        "form": NewTaskForm()
    })