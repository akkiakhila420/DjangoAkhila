from django.db import models
# Create your models here.
from django.db import models
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    class Meta:
        abstract=True

class Student(ContactInfo):
    rollno=models.IntegerField()
    mark=models.IntegerField()
class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()

class BasicModel(models.Model):
    f1=models.CharField(max_length=64)
    f2=models.CharField(max_length=64)
    f3=models.CharField(max_length=64)
class StandardModel(BasicModel):
    f4=models.CharField(max_length=64)
    f5=models.CharField(max_length=64)

class Person(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()

class Employee(Person):
    eno=models.IntegerField()
    esal=models.FloatField()
class Manager(Employee):
    exp=models.IntegerField()
    team_size=models.IntegerField()

class Parent1(models.Model):
    parent1_id=models.AutoField(primary_key=True)
    f1=models.CharField(max_length=64)
    f2=models.CharField(max_length=64)

class Parent2(models.Model):
    parent2_id = models.AutoField(primary_key=True)
    f3 = models.CharField(max_length=64)
    f4 = models.CharField(max_length=64)

class Child(Parent1,Parent2):
    f5 = models.CharField(max_length=64)
    f6 = models.CharField(max_length=64)

from django.db import models
class CustomManager(models.Manager):
    def get_queryset(set):
        return super().get_queryset().order_by('-eno')
    def get_emp_sal_range(self, esal1, esal2):  # 2-args
        return super().get_queryset().filter(esal__range=(esal1, esal2))
    def get_employees_sorted_by(self, param):  # 1-args
        return super().get_queryset().order_by(param)

class Employees(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager()

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=2000)

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lt=2000)

class Employees(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager1()

class ProxyEmployees1(Employees):
    objects = CustomManager2()
    class Meta:
        proxy=True
class ProxyEmployees2(Employees):
    objects = CustomManager3()
    class Meta:
        proxy = True

