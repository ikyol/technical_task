from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

from .models import Task

User = get_user_model()


class TaskViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='user@examlpe.com', password='password')
        self.user2 = User.objects.create_user(email='user2@examlpe.com', password='password')
        self.client.force_authenticate(user=self.user)
        self.task_data = {'title': 'Test Task', 'description': 'Test Description', 'assigned_to': self.user.id,
                          'created_by': self.user2.id}

    def test_create_task(self):
        response = self.client.post('/api/v1/task/', data=self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        response = self.client.get('/api/v1/task/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        print(self.user2)
        task = Task.objects.create(title='Old Task', description='Old Description', assigned_to=self.user,
                                   created_by=self.user2)
        response = self.client.patch(f'/api/v1/task/{task.id}/',
                                     {'title': 'New Task', 'description': 'New Description',
                                      'created_by': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=task.id).title, 'New Task')

    def test_delete_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description', assigned_to=self.user,
                                   created_by=self.user2)
        response = self.client.delete(f'/api/v1/task/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
