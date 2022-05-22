# Generated by Django 4.0.2 on 2022-05-18 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='tasks.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]