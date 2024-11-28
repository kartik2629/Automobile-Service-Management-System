from ast import pattern
from email import message
import re
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator,validate_slug


# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=False,blank=False)
    address = models.CharField(max_length=40,null=False,validators=[RegexValidator('[A-Za-z]',message= "Enter only Alphabets")])
    mobile = models.CharField(max_length=15,null=False,validators=[RegexValidator(
            r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
            message='Enter Valid Indian Number'
        )])
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
    

class Mechanic(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/MechanicProfilePic/',null=False,blank=False)
    address = models.CharField(max_length=40,null=False,validators=[RegexValidator('[A-Za-z]',message= "Enter only Alphabets")])
    mobile = models.CharField(max_length=10,null=False,validators=[RegexValidator(
            r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
            message='Enter Valid Indian Number'
        )])
    skill = models.CharField(max_length=500,null=False)
    salary=models.PositiveIntegerField(null=False)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    cat=(('Two wheeler with Gear','Two wheeler with Gear'),('Two wheeler without Gear','Two wheeler without Gear'),('Three wheeler','Three wheeler'),('Four wheeler','Four wheeler'))
    category=models.CharField(max_length=50,choices=cat)

    vehicle_no=models.CharField(max_length=10, null=False)
    vehicle_name = models.CharField(max_length=40,null=False)
    vehicle_model = models.CharField(max_length=40,null=False)
    vehicle_brand = models.CharField(max_length=40,null=False)

    problem_description = models.CharField(max_length=500,null=False)
    date=models.DateField(auto_now=True)
    cost=models.PositiveIntegerField(null=True)

    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)

    stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=False)

    def __str__(self):
        return self.problem_description

class Attendance(models.Model):
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now=True)
    present_status = models.CharField(max_length=10)

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40,null=False)
    message=models.CharField(max_length=500,null=False)