from django.test import TestCase
from django.contrib.auth import get_user_model

from .serializers import CreateUserSerializer, UpdateUserSerializer

User = get_user_model()


class CreateUserSerializerTestCase(TestCase):
    def test_create_user_serializer(self):
        user_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'testpassword'
        }
        serializer = CreateUserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertFalse(user.is_active)


class UpdateUserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpassword'
        )

    def test_update_user_serializer(self):
        update_data = {
            'email': 'updated@example.com',
            'name': 'Updated User',
            'is_active': True
        }
        serializer = UpdateUserSerializer(instance=self.user, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.email, 'updated@example.com')
        self.assertEqual(updated_user.name, 'Updated User')


