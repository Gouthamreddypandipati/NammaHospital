from django.urls import path
from . import views

urlpatterns=[
    # getting the data
    path('Users/',views.Userdata,name='user'),
    path('Docters/',views.Doctersdata,name='Docters'),
    path('Reports/<int:pk>/',views.Reports_user,name='Reports'),
    path('Courses/<int:pk>/',views.Courses_users,name='Courses'),
    path('Docterpatient/<int:pk>/',views.Docter_patients,name='DP'),
    path('Tests/<int:pk>/',views.Tests_data,name='tests'),
    

    # posting the data
    path('createuser/',views.CreateUser,name='createuser'),
    # creating docter
    path('createdocter/',views.CreateDocter,name='createdocter'),
]