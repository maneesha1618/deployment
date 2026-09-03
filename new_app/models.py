from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=50)
    age= models.IntegerField()
    position = models.CharField(max_length=100)
    department=models.CharField(max_length=100,default = 'IT')
    salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        # return self.name
        return f" name ={self.name} - Age = {self.age} Position = {self.position} - {self.department} Salary = {self.salary}"


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.CharField(max_length=3)

    def __str__(self):
        return f" Name = {self.name} - Age = {self.age} - Grade = {self.grade}"

