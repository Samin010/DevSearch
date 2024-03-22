from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects, name="projects"),
    path('project/<str:key>/',views.singleProject,name='singleProject'),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:key>/',views.updateProject,name="update-project"),
    path('delete-project/<str:key>/',views.deleteProject,name="delete-project"),
]
