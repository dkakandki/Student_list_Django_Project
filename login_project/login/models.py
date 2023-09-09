from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_num = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
    # def create_student(self, username, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", False)
    #     extra_fields.setdefault("is_superuser", False)
    #     return self._create_user(username, email, password, **extra_fields)
    
    
    
class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mother_name =  models.CharField(max_length=100)
    father_name =  models.CharField(max_length=100)
    phone_num =  models.IntegerField(null=False)
    
    def __str__(self):
        return self.mother_name