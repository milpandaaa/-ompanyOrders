from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            }


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','project', 'date_begin', 'date_finish', 'is_finish']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.TextInput(attrs={'class': 'form-control'}),
            'date_begin': forms.TextInput(attrs={'class': 'form-control'}),
            'date_finish': forms.TextInput(attrs={'class': 'form-control'}),
            'is_finish': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'salary', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Company_form(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address','number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmployeeTask_form(forms.ModelForm):
    class Meta:
        model = EmployeeTask
        fields = ['employee', 'task']
        widgets = {
            'employee': forms.TextInput(attrs={'class': 'form-control'}),
            'task': forms.TextInput(attrs={'class': 'form-control'}),
        }
