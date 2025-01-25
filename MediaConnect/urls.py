

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('about', views.about, name='about'),
      path('inquiry/', views.inquiry, name='inquiry'),
      path('web-dev/', views.web_dev, name='web_dev'),
      path('team/', views.team, name='team'),
      path('nav/', views.nav, name='nav'),   
      path('offline/', views.offline, name='offline'),   
      path('online/', views.online, name='online'), 
       path('funding/', views.funding, name='funding'), 
       path('temp/', views.temp, name='temp'), 
]
