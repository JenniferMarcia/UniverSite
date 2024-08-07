from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="password"
        )

        # Get tokens for the user
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "password"},
        )
        self.access_token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # URLs for CustomUser views
        self.user_list_url = reverse("user-list")
        self.user_detail_url = reverse("user-detail", kwargs={"pk": self.user.pk})
        self.user_update_url = reverse("user-update", kwargs={"pk": self.user.pk})
        self.user_delete_url = reverse("user-delete", kwargs={"pk": self.user.pk})
        self.logout_url = reverse("logout")
        self.update_password_url = reverse(
            "update-password", kwargs={"pk": self.user.pk}
        )

    def tearDown(self):
        self.client.logout()

    def test_user_list(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_user_detail(self):
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.user.pk)

    def test_user_update(self):
        data = {"email": "new_email@test.com"}
        response = self.client.patch(self.user_update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_user = CustomUser.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.email, "new_email@test.com")

    def test_user_delete(self):
        response = self.client.delete(self.user_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(pk=self.user.pk)

    def test_logout(self):
        refresh = RefreshToken.for_user(self.user)  # Generate refresh token
        response = self.client.post(
            self.logout_url, {"refresh": str(refresh)}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertIn("User logout successfully", response.data["message"])

    def test_update_password(self):
        data = {"current_password": "password", "new_password": "new_password"}
        response = self.client.post(self.update_password_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("new_password"))
