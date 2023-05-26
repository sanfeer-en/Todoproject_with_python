from django.shortcuts import render , redirect
from .models import *
from . forms import TodoForm
# LISTVIEW
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse, reverse_lazy

#class base generic views
class TasklistView(ListView):
    model=Task
    template_name ='home.html'
    context_object_name = 'task1'
class TaskDetailView(DetailView):
    model=Task
    template_name ='details.html'
    context_object_name = 'task1'
class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task1'
    Date = models.DateField()
    fields =('Name','Priority','Date')


    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name ='delete.html'
    success_url = reverse_lazy('cbvhome')
      

# Create your views here.
def add(request):
    taskk=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task' , '')
        priority = request.POST.get('priority' , '') 
        date = request.POST.get('date' , '')
        task = Task(Name =name, Priority = priority ,Date = date)
        task.save()
    return render(request,'home.html',{'task1':taskk })

# def details(request):
    
#     return render(request,'details.html',)
def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
    
