from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('intro/', views.intro, name='intro'),
    path('resume/', views.resume, name='resume'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('goals/', views.goals, name='goals')
]