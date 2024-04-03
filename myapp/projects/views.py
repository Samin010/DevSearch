from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
# Create your views here.
from .utils import searchProjects, paginateProjects

from django.contrib import messages


def projects(request):
  
  projects, search_query = searchProjects(request)
  custom_range, projects=paginateProjects(request,projects,6)
  
  context={'projects':projects,'search_query':search_query,'custom_range': custom_range}
  return render(request,'projects/projects.html',context)

def singleProject(request,key):
  projectObj=Project.objects.get(id=key)
  form=ReviewForm()
  
  if request.method=='POST':
    form =ReviewForm(request.POST)
    review=form.save(commit=False)
    review.project=projectObj
    review.owner=request.user.profile
    review.save()
    
    projectObj.getVoteCount
    
    messages.success(request, 'Your review was succesfully submitted')
    
    return redirect('singleProject' , key=projectObj.id)  
    
  
  return render(request,'projects/single-project.html',{'project':projectObj,'form':form})

@login_required(login_url="login")
def createProject(request):
   profile=request.user.profile
   form=ProjectForm()
   
   if request.method=='POST':
     form=ProjectForm(request.POST,request.FILES)
     if form.is_valid():
       project=form.save(commit=False)
       project.owner=profile
       project.save()
      
       return redirect('account')
   
   context={'form':form}
   return render(request,"projects/project_form.html",context)
 
 
@login_required(login_url="login")
def updateProject(request,key):
   profile=request.user.profile
   project=profile.project_set.get(id=key)
   form=ProjectForm(instance=project)
   
   if request.method=='POST':
     form=ProjectForm(request.POST,request.FILES,instance=project)
     if form.is_valid():
       form.save()
       return redirect('account')
   
   context={'form':form}
   return render(request,"projects/project_form.html",context)
  
@login_required(login_url="login")
def deleteProject(request,key):
  profile=request.user.profile
  project=profile.project_set.get(id=key)
  if request.method=='POST':
    project.delete()
    return redirect('projects')
  context={'object':project}
  return render(request,"delete_template.html",context)  
  