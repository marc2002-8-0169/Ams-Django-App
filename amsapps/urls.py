from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add/', views.add, name='add'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('studentupdate', views.studentupdate, name='studentupdate'),
    path('studentinfo/', views.studentinfo, name='studentinfo'),

]
