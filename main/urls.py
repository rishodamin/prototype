from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('hire/<str:ind>', views.hire, name='hire'),
    path('book/<str:ind>', views.book, name='book'),
    path('postjobs/<categ>', views.postjobs, name='postjobs'),
    path('getjobs/<categ>', views.getjobs, name='getjobs'),
    path('jobdetails/<jobid>', views.jobdetails, name='jobdetails')
]