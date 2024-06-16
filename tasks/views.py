from django.shortcuts import render, redirect
from .models import Goal
from .forms import Taskform

def index(request):
    tasks = Goal.objects.all()
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks': tasks,'Taskform':form}
    return render(request , 'tasks.html' , context)

def updateTask(request , pk):
    goal= Goal.objects.get(id=pk)
    

    if request.method == 'POST':
        form = Taskform(request.POST , instance=goal)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        
        form = Taskform(instance=goal)


    context = {'Taskform':form}
    return render(request , 'update.html' , context)

def deleteTask(request , pk):
    goal= Goal.objects.get(id=pk)


    if request.method == 'POST':
        goal.delete() 

        return redirect('/')
    
    context = {'goal': goal}
    return render(request , 'delete.html' , context)




    
 

 