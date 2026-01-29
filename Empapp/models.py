from django.db import models

# Create your models here.
class EmployeeDb(models.Model):
    Emp_id=models.AutoField(primary_key=True)

    name=models.CharField(max_length=100,null=True,blank=True)
    company=models.CharField(max_length=100,null=True,blank=True)
    Designation=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)