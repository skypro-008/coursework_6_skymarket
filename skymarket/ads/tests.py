from ads.models import Ad, Comment
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import User


class AdTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="test",
            first_name="Test",
            last_name="User",
            phone="79991234567",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)
        self.ad = Ad.objects.create(
            title="Test Ad",
            description="Test description",
            price=1000,
            author=self.user,
        )

    def test_create_ad(self):
        """Тестирование создания объявления."""
        data = {
            "title": "Test Ad 2",
            "description": "Test description 2",
            "price": 1000,
            "author": self.user.id,
        }
        response = self.client.post("/api/ads/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ad.objects.count(), 2)
        self.assertTrue(Ad.objects.all().exists())

    def test_list_ads(self):
        """Тестирование получения списка объявлений."""
        response = self.client.get("/api/ads/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_retrieve_ad(self):
        """Тестирование получения одного объявления."""
        response = self.client.get(f"/api/ads/{self.ad.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.ad.title)

    def test_update_ad(self):
        """Тестирование изменения объявления."""
        data = {"title": "Updated Test Ad"}
        response = self.client.patch(f"/api/ads/{self.ad.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Test Ad")

    def test_destroy_ad(self):
        """Тестирование удаления объявления."""
        response = self.client.delete(f"/api/ads/{self.ad.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.count(), 0)


class CommentTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="test",
            first_name="Test",
            last_name="User",
            phone="79991234567",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)
        self.ad = Ad.objects.create(
            title="Test Ad",
            description="Test description",
            price=1000,
            author=self.user,
        )
        self.comment = Comment.objects.create(
            text="Test comment",
            author=self.user,
            ad=self.ad,
        )

    def test_create_comment(self):
        """Тестирование создания комментария."""
        data = {
            "text": "Test comment 2",
            "author": self.user.id,
            "ad": self.ad.id,
        }
        response = self.client.post(f"/api/ads/{self.ad.id}/comments/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertTrue(Comment.objects.all().exists())

    def test_list_comment(self):
        """Тестирование получения списка комментариев."""
        response = self.client.get(f"/api/ads/{self.ad.id}/comments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.all().count(), 1)

    def test_retrieve_comment(self):
        """Тестирование получения одного комментария."""
        response = self.client.get(f"/api/ads/{self.ad.id}/comments/{self.comment.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["text"], self.comment.text)

    def test_update_comment(self):
        """Тестирование изменения комментария."""
        data = {"text": "Updated Test comment"}
        response = self.client.patch(
            f"/api/ads/{self.ad.id}/comments/{self.comment.id}/", data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["text"], "Updated Test comment")

    def test_delete_comment(self):
        """Тестирование удаления комментария."""
        response = self.client.delete(
            f"/api/ads/{self.ad.id}/comments/{self.comment.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
