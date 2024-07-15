from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, FieldOfStudy

from UserApp.models import CustomUser


class CourseUpdateDeleteTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a CustomUser
        self.custom_user = CustomUser.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a Course associated with the CustomUser
        self.course = Course.objects.create(course_name="Course test")
        self.course.custom_users.add(
            self.custom_user
        )  # Utilisation correcte de custom_users

        # Valid payload for updating Course
        self.valid_payload = {
            "course_name": "new name Course",
            "prerequisites": "Nouveaux prérequis",
            "details": "new details",
            "custom_users": [
                self.custom_user.pk
            ],  # Utilisation correcte de custom_users et de l'ID de l'utilisateur personnalisé
        }

    def test_update_course(self):
        # Authenticate the CustomUser
        self.client.force_authenticate(user=self.custom_user)

        # URL pour mettre à jour l'instance de Course
        url = reverse(
            "Course-update", kwargs={"pk": self.course.pk}
        )  # Utilisation de "Course-update" ici

        # Faire une requête PUT avec le payload valide
        response = self.client.put(url, self.valid_payload, format="json")

        # Vérifier que le code d'état de la réponse est HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_update_course(self):
        # Créer un nouvel utilisateur personnalisé non associé au cours
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # Authentifier cet utilisateur personnalisé non autorisé
        self.client.force_authenticate(user=unauthorized_custom_user)

        # URL pour mettre à jour l'instance de Course
        url = reverse(
            "Course-update", kwargs={"pk": self.course.pk}
        )  # Utilisation de "Course-update" ici

        # Faire une requête PUT avec le payload valide
        response = self.client.put(url, self.valid_payload, format="json")

        # Vérifier que le code d'état de la réponse est HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_course(self):
        # Authentifier l'utilisateur personnalisé
        self.client.force_authenticate(user=self.custom_user)

        # URL pour supprimer l'instance de Course
        url = reverse(
            "Course-delete", kwargs={"pk": self.course.pk}
        )  # Utilisation de "Course-delete" ici

        # Faire une requête DELETE
        response = self.client.delete(url)

        # Vérifier que le code d'état de la réponse est HTTP 204 No Content (suppression réussie)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_delete_course(self):
        # Créer un nouvel utilisateur personnalisé non associé au cours
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # Authentifier cet utilisateur personnalisé non autorisé
        self.client.force_authenticate(user=unauthorized_custom_user)

        # URL pour supprimer l'instance de Course
        url = reverse(
            "Course-delete", kwargs={"pk": self.course.pk}
        )  # Utilisation de "Course-delete" ici

        # Faire une requête DELETE
        response = self.client.delete(url)

        # Vérifier que le code d'état de la réponse est HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FieldOfStudyUpdateDeleteTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Créer un utilisateur personnalisé
        self.custom_user = CustomUser.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Créer un cours associé à l'utilisateur personnalisé
        self.course = Course.objects.create(course_name="Course test")
        self.course.custom_users.add(self.custom_user)

        # Créer un domaine d'étude associé au cours
        self.field_of_study = FieldOfStudy.objects.create(
            field_name="FieldOfStudy test", course=self.course
        )

        # Payload valide pour mettre à jour FieldOfStudy
        self.valid_payload = {"field_name": "Nouveau nom de FieldOfStudy"}

    def test_update_field_of_study(self):
        # Authentifier l'utilisateur personnalisé
        self.client.force_authenticate(user=self.custom_user)

        # URL pour mettre à jour l'instance de FieldOfStudy
        url = reverse("FieldOfStudy-update", kwargs={"pk": self.field_of_study.pk})

        # Faire une requête PUT avec le payload valide
        response = self.client.put(url, self.valid_payload, format="json")

        # Vérifier que le code d'état de la réponse est HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_update_field_of_study(self):
        # Créer un nouvel utilisateur personnalisé non associé au cours
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # Authentifier cet utilisateur personnalisé non autorisé
        self.client.force_authenticate(user=unauthorized_custom_user)

        # URL pour mettre à jour l'instance de FieldOfStudy
        url = reverse("FieldOfStudy-update", kwargs={"pk": self.field_of_study.pk})

        # Faire une requête PUT avec le payload valide
        response = self.client.put(url, self.valid_payload, format="json")

        # Vérifier que le code d'état de la réponse est HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_field_of_study(self):
        # Authentifier l'utilisateur personnalisé
        self.client.force_authenticate(user=self.custom_user)

        # URL pour supprimer l'instance de FieldOfStudy
        url = reverse("FieldOfStudy-delete", kwargs={"pk": self.field_of_study.pk})

        # Faire une requête DELETE
        response = self.client.delete(url)

        # Vérifier que le code d'état de la réponse est HTTP 204 No Content (suppression réussie)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_delete_field_of_study(self):
        # Créer un nouvel utilisateur personnalisé non associé au cours
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # Authentifier cet utilisateur personnalisé non autorisé
        self.client.force_authenticate(user=unauthorized_custom_user)

        # URL pour supprimer l'instance de FieldOfStudy
        url = reverse("FieldOfStudy-delete", kwargs={"pk": self.field_of_study.pk})

        # Faire une requête DELETE
        response = self.client.delete(url)

        # Vérifier que le code d'état de la réponse est HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
