from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    date_begin = models.DateField()
    date_finish = models.DateField()
    is_finish = models.BooleanField()


class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=50)
    salary = models.FloatField()
    company = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.IntegerField()


class EmployeeTask(models.Model):
    employee = models.CharField(max_length=150)
    task = models.CharField(max_length=50)


# Create your models here.
