from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):
    tries=forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"try/index.html",{
        "tasks": request.session["tasks"]
    })
def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            tasks=form.cleaned_data["tries"]
            request.session["tasks"]+=[tasks]
            return HttpResponseRedirect(reverse("try:index"))

        else :
              return render(request,"try/add.html",{
                   "form": form
              })

    return render(request,"try/add.html",{
        "form" :NewTaskForm()
    })

