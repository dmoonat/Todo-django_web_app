from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def index(request):
    todos=Todo.objects.all()[:10]
    context={
        'name':'dmoonat',
        'todos':todos
        }
    return render(request,'index.html',context)
    #return HttpResponse('Hello World')

def details(request,id):
    todo=Todo.objects.get(id=id)
    context={
        
        'todo':todo
        }
    return render(request,'details.html',context)

def add(request):
    if request.method=='POST':
        title=request.POST['title']
        text=request.POST['text']
        schedule=request.POST['schedule']
        todo=Todo(title=title,text=text,schedule=schedule)
        todo.save()
        return redirect('/todos')
    else:
        return render(request,'add.html',{})

def delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos')

def edit(request,id):
    todo=Todo.objects.get(id=id)
    schedule=str(todo.schedule)
    schedule=schedule.split('+')[0].replace(' ','T')
    #print(schedule)
    context={
        'edit':True,
        'title':todo.title,
        'text':todo.text,
        'schedule':schedule
        }
    delete(request,id)
    return render(request,'add.html',context)

def complete(request,id):
    todo=Todo.objects.get(id=id)
    todo.completed=True
    todo.save()
    return redirect('/todos')

def incomplete(request,id):
    todo=Todo.objects.get(id=id)
    todo.completed=False
    todo.save()
    return redirect('/todos')
