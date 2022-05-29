from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Category, Task

class TaskInline(admin.StackedInline):
    model = Task
    extra = 0
    
class TaskAdmin(UserAdmin):   
    inlines = [TaskInline]

admin.site.register(User, TaskAdmin)
admin.site.register(Category)
admin.site.register(Task)