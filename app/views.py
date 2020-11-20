from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"
    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout(request):
    return render(request, "logout.html")



def projects(request):
    context = {"data_p": Project.objects.all()}
    return render(request, "projects.html", context)


def project(request, project_name):
    try:
        data_t = Task.objects.filter(project=project_name)
        project = project_name
        return render(request, "project.html", {"data_t": data_t, "project": project,
                                                "data_et": EmployeeTask.objects.all()})
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Тask not found</h2>")


def task_delete(request, task_id):
    try:
        c = Task.objects.get(id=task_id)
        c.delete()
        context = {}
        context["data_t"] = Task.objects.all()
        return render(request, 'projects.html', context)
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")


@csrf_protect
def task_edit(request, task_id):
    try:
        data_t = Task.objects.get(id=task_id)
        print(data_t)
        data_p = Project.objects.all()
        if request.method == "POST":
            data_t.name = request.POST.get("name")
            data_t.project = request.POST.get("project")
            data_t.date_begin = request.POST.get("date_begin")
            data_t.date_finish = request.POST.get("date_finish")
            data_t.is_finish = request.POST.get("is_finish")
            data_t.save()
            return render(request, 'projects.html', {"data_p":data_p})
        else:
            return render(request, "task_edit.html", {"data_t": data_t, "data_p": data_p})
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")


def task_add(request):
    context = {"data_p" : Project.objects.all()}
    form = Task_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "task_add.html", context)


def employee_add(request):
    form = Employee_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form, 'data_c': Company.objects.all()}
    return render(request, "employee_add.html",context)


def employees(request):
    context = {"data_e": Employee.objects.all()}
    return render(request, "employees.html", context)


def project_add(request):
    form = Project_form(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        form.save()
    context = {}
    context['form'] = form
    return render(request, "project_add.html")


def company_add(request):
    form = Company_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "company_add.html", context)


def companies(request):
    context = {"data_c": Company.objects.all()}
    return render(request, "companies.html", context)


def employeeTask(request):
    form = EmployeeTask_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form, 'data_e':Employee.objects.all(), 'data_t':Task.objects.all()}
    return render(request, "employeeTask_add.html", context)
# Create your views here.
