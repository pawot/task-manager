from unicodedata import name
from django.test import TestCase
from django.contrib.auth.models import User
from .models import User, Category, Task
from django.test.client import Client

class TaskTestCase(TestCase):

    def setUp(self):
    
        user = User.objects.create_superuser("p", "p@p.com", "p")
        category = Category.objects.create(name="Chores")

        t1 = Task.objects.create(title="Buy milk", user=user, category=category, active=True)
        t1 = Task.objects.create(title="Go for a walk and then play football untill exhausted and finally take a shower and go to bed", user=user, category=category, active=False)

    def test_valid_task(self):
        t = Task.objects.get(active=False)
        self.assertTrue(t.is_valid_task())

    def test_index(self):
        t = Task.objects.get(active=False)
        c = Client()
        response = c.get(f"/change/{t.id}")
        self.assertEqual(response.status_code, 302)