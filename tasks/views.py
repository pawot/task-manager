from threading import activeCount
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import User, Category, Task
from .forms import NewTaskForm


class index(ListView):
    """ Render index page or user's tasks if user is authenticated """
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = User.objects.get(pk=self.request.user.id)
            queryset = {'activeTasks': user.userTasks.filter(active=True), 
                        'finishedTasks': user.userTasks.filter(active=False)}
            return queryset

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return 'tasks/my_tasks.html'
        return 'tasks/index.html'


'''    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        activeTasks = user.userTasks.filter(active=True)
        finishedTasks = user.userTasks.filter(active=False)
        return render(request, "tasks/my_tasks.html", {
            "activeTasks": activeTasks,
            "finishedTasks": finishedTasks,
        })
    else:
        return render(request, "tasks/index.html")
'''

def register(request):
    """ Register new user in the app """

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "tasks/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(request, "tasks/register.html", {
                "message": "This username already exist."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tasks/register.html")


def login_view(request):
    """ Log user in the app if username and password are correct """

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tasks/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def task_change(request, task_id):
    """ Set active field in Task model to false or true  """

    task = Task.objects.get(pk=task_id)
    user = User.objects.get(pk=request.user.id)
    activeTasks = user.userTasks.filter(active=True)
    if task in activeTasks: 
        task.active = False
        task.save()
    else:
        task.active = True
        task.save()
    return HttpResponseRedirect(reverse("index"))

@login_required
def delete(request, task_id):
    """ Remove task from database """
    task = Task.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("index"))

@login_required
def new_task(request):
    """ Add new task to database """

    if request.method == "POST":
        ''' 
        title = request.POST["title"]
        category_id = int(request.POST["category"])
        category = Category.objects.get(pk=category_id)
        deadline = request.POST["deadline"]
        '''
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            deadline = form.cleaned_data['deadline']
            user = User.objects.get(pk=request.user.id)
            task = Task(title=title, category=category, deadline=deadline, user=user, active=True)
            task.save()
        return HttpResponseRedirect(reverse("index"))
    
    #categories = Category.objects.all()
    form = NewTaskForm()
    return render(request, "tasks/new_task.html", {
        'form': form
        })

@login_required
def category(request, category_name):
    """ Display tasks in particular category """

    category = Category.objects.get(name=category_name)
    tasks = category.categoryTasks.filter(user=request.user.id)
    activeTasks = tasks.filter(active=True)
    finishedTasks = tasks.filter(active=False)

    return render(request, "tasks/category_tasks.html", {
            "activeTasks": activeTasks,
            "finishedTasks": finishedTasks,
            "category": category
        })