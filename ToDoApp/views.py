from django.shortcuts import render,redirect
from . forms import TaskForm 
from .models import Task
# Create your views here.
def Create(request):
  create = TaskForm()
  database = Task.objects.all() 
  if request.method == "POST":
    create = TaskForm(request.POST)
    if create.is_valid():
      create.save()
      return redirect('/')
  context = {'create':create,'database':database}
  return render(request,"ToDoApp/index.html",context)


def Update(request,id):
  database = Task.objects.get(id=id)  
  create = TaskForm(instance=database)
  if request.method == "POST":
    create = TaskForm(request.POST,instance=database)
    if create.is_valid():
      create.save()
      return redirect('/')
  context = {'create':create,'database':database}
  return render(request,"ToDoApp/update.html",context)
  


def Delete(request,id):
  database = Task.objects.get(id=id)  
  if request.method == "POST":
    database.delete()
    return redirect('/')
  context = {'database':database}
  return render(request,"ToDoApp/delete.html",context)
  