from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Task

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Task)