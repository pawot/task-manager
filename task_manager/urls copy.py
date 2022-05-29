from django.urls import path
from tasks.views import index

from . import views

urlpatterns = [
    path("", index.as_view(), name="index"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("new_task", views.new_task, name="new_task"),
    path("change/<str:task_id>", views.task_change, name="task_change"),
    path("delete/<str:task_id>", views.delete, name="delete"),
    path("category/<str:category_name>", views.category, name="category")
]
