from django.shortcuts import render, redirect
from first_app.forms import AddTaskForm
from first_app.models import AddTaskModel
# Create your views here.
# user name todo 
def home(request):
    return render(request, 'home.html')

def addTask(request):
    if request.method == 'POST':
        task = AddTaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_task') 
    else:
        task = AddTaskForm()
    return render(request, 'add_task.html', {'AddTask': task})

def ShowTask(request):
    task = AddTaskModel.objects.all()
    print(task)
    return render(request, 'show_task.html', {'data':task} )

def editTask(request,id):
    task_model = AddTaskModel.objects.get(pk = id)
    task_form = AddTaskForm(instance = task_model)
    if request.method == 'POST':
        task = AddTaskForm(request.POST, instance = task_model)
        if task.is_valid():
            task.save()
            return redirect('show_task')
    return render(request, 'add_task.html',  {'AddTask': task_form})

def DeleteTask(request,id):
    task = AddTaskModel.objects.get(pk=id).delete()
    return redirect('show_task')

def CompTask(request,id):
    task_model = AddTaskModel.objects.get(pk = id)
    task_model.status='complated'
    task_model.tarck = True
    task_model.save()
    return redirect('comtask')

def Comp(request):
    task = AddTaskModel.objects.all()
    print(task)
    return render(request, 'com.html', {'data':task} )