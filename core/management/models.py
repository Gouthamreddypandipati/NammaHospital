from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# from haystack.fields import ListTextField
from django.contrib.auth.hashers import make_password
# Create your models here.


# user model
class UserModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name=models.CharField(blank=True,null=True,max_length=128)
    email=models.EmailField(blank=True,null=True,unique=True)
    age=models.IntegerField(blank=True,null=True)
    mobile_number = models.CharField(max_length=10,blank=True,null=True,unique=True)
    password = models.CharField(max_length=128,blank=True,null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# docter model
class Doctor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name=models.CharField(blank=True,null=True,max_length=128)
    total_experience=models.DecimalField(blank=True,null=True,max_digits=7, decimal_places=2)
    email=models.EmailField(blank=True,null=True,unique=True)
    age=models.IntegerField(blank=True,null=True)
    specialization=models.CharField(blank=True,null=True,max_length=128)
    Hospital_name=models.CharField(blank=True,null=True,max_length=128)
    mobile_number = models.CharField(max_length=10,unique=True)
    password = models.CharField(blank=True,null=True,max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Reports
class Reports(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user=models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    type=models.CharField(blank=False,null=False,max_length=300)
    #files
    medicines=models.JSONField(blank=False,null=False)
    Days=models.IntegerField(blank=False,null=False,default=0)
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.type


# medication
class Courses(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)  
    Report_id=models.ForeignKey(Reports,on_delete=models.SET_NULL,null=True)  
    Number_of_days_completed=models.IntegerField(blank=False,null=False,default=0)
    progress=models.BooleanField(blank=True,null=True)



# linking the user with the docters 
class Docterpatient(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
# tests to be taken
class Tests(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    Test_to_be_taken=models.CharField(blank=True,null=True,max_length=300)
    Date=models.DateTimeField(blank=True,null=True)



    