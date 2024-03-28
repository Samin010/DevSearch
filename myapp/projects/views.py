from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm
# Create your views here.





def projects(request):
  projects=Project.objects.all()
  context={'projects':projects}
  return render(request,'projects/projects.html',context)

def singleProject(request,key):
  projectObj=Project.objects.get(id=key)
  return render(request,'projects/single-project.html',{'project':projectObj})

@login_required(login_url="login")
def createProject(request):
   form=ProjectForm()
   
   if request.method=='POST':
     form=ProjectForm(request.POST,request.FILES)
     if form.is_valid():
       form.save()
       return redirect('projects')
   
   context={'form':form}
   return render(request,"projects/project_form.html",context)
 
 
@login_required(login_url="login")
def updateProject(request,key):
   project=Project.objects.get(id=key)
   form=ProjectForm(instance=project)
   
   if request.method=='POST':
     form=ProjectForm(request.POST,request.FILES,instance=project)
     if form.is_valid():
       form.save()
       return redirect('projects')
   
   context={'form':form}
   return render(request,"projects/project_form.html",context)
  
@login_required(login_url="login")
def deleteProject(request,key):
  project=Project.objects.get(id=key)
  if request.method=='POST':
    project.delete()
    return redirect('projects')
  context={'object':project}
  return render(request,"projects/delete_template.html",context)  
  