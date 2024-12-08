from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import User


class UserTestCase(APITestCase):
    """Тесты для пользователя"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="test",
            first_name="Test",
            last_name="User",
            phone="+79991234567",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """Тестирование создания пользователя."""
        data = {
            "email": "test1@example.com",
            "password": "test1234!!!",
            "first_name": "Test1",
            "last_name": "User1",
            "phone": "+79991234567",
            "is_active": True,
        }
        response = self.client.post("/api/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.all().exists())

    def test_list_users(self):
        """Тестирование получения списка пользователей."""
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 1)

    def test_retrieve_users(self):
        """Тестирование получения одного пользователя."""
        response = self.client.get(f"/api/users/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_users(self):
        """Тестирование изменения пользователя."""
        data = {"first_name": "Test 1"}
        response = self.client.patch(f"/api/users/{self.user.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Test 1")
