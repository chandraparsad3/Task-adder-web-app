from . import views
from django.urls import path

app_name="try"
urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.add,name="add")
]