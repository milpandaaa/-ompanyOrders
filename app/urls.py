from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout, name="logout_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', projects, name="projects_url"),
    path('project/<slug:project_name>', project, name="project_url"),
    path('task_delete/<int:task_id>', task_delete, name="task_delete_url"),
    path('task_edit/<int:task_id>', task_edit, name="task_edit_url"),
    path('task_add', task_add, name="task_add_url"),
    path('project_add', project_add, name="project_add_url"),
    path('employees', employees, name="employees_url"),
    path('employee_add', employee_add, name="employee_add_url"),
    path('companies', companies, name="companies_url"),
    path('company_add', company_add, name="company_add_url"),
    path('EM', employeeTask, name="employeeTask_url"),
]