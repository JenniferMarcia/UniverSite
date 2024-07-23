from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, FieldOfStudy

from Users.models import CustomUser


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
            "custom_users": [self.custom_user.pk],
        }

    def test_update_course(self):
        # Authenticate the CustomUser
        self.client.force_authenticate(user=self.custom_user)

        # URL pour mettre à jour l'instance de Course
        url = reverse(
            "Course-update", kwargs={"pk": self.course.pk}
        )  #  we use "Course-update" here

        # Make a PUT request with the valid payload
        response = self.client.put(url, self.valid_payload, format="json")

        # Vérifier que le code d'état de la réponse est HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_update_course(self):
        # Create a new user for create a new user associated to Course
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="test", password="testpassword"
        )

        # Authenticate this unauthorized user
        self.client.force_authenticate(user=unauthorized_custom_user)

        # Update course URL
        url = reverse(
            "Course-update", kwargs={"pk": self.course.pk}
        )  # Utilisation de "Course-update" ici

        # PUT request with valid playload
        response = self.client.put(url, self.valid_payload, format="json")

        # Verrify if state code  equals HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_course(self):
        # Create a user not associated with any course
        self.client.force_authenticate(user=self.custom_user)

        # URL for deleting the course
        url = reverse("Course-delete", kwargs={"pk": self.course.pk})

        # send a DELETE request
        response = self.client.delete(url)

        # Verrify if state code equals HTTP 204 No Content (suppression réussie)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_delete_course(self):
        # Create an user with no course
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # authenticate this user  with no course
        self.client.force_authenticate(user=unauthorized_custom_user)

        # DELETE course
        url = reverse("Course-delete", kwargs={"pk": self.course.pk})

        # DELETE request
        response = self.client.delete(url)

        # Verrify if state code  if not equals HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FieldOfStudyUpdateDeleteTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a custom user
        self.custom_user = CustomUser.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a course associated with the custom user
        self.course = Course.objects.create(course_name="Course test")
        self.course.custom_users.add(self.custom_user)

        # Create a field of study associated with the course
        self.field_of_study = FieldOfStudy.objects.create(
            field_name="FieldOfStudy test", course=self.course
        )

        # Valid payload to update FieldOfStudy
        self.valid_payload = {"field_name": "New FieldOfStudy name"}

    def test_update_field_of_study(self):
        # Authenticate the custom user
        self.client.force_authenticate(user=self.custom_user)

        # URL to update the FieldOfStudy instance
        url = reverse("FieldOfStudy-update", kwargs={"pk": self.field_of_study.pk})

        # Make a PUT request with the valid payload
        response = self.client.put(url, self.valid_payload, format="json")

        # Check that the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_update_field_of_study(self):
        # Create a new custom user not associated with the course
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # Authenticate this unauthorized custom user
        self.client.force_authenticate(user=unauthorized_custom_user)

        # URL to update the FieldOfStudy instance
        url = reverse("FieldOfStudy-update", kwargs={"pk": self.field_of_study.pk})

        # Make a PUT request with the valid payload
        response = self.client.put(url, self.valid_payload, format="json")

        # Check that the response status code is HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_field_of_study(self):
        # Authenticate the custom user
        self.client.force_authenticate(user=self.custom_user)

        # URL to delete the FieldOfStudy instance
        url = reverse("FieldOfStudy-delete", kwargs={"pk": self.field_of_study.pk})

        # Make a DELETE request
        response = self.client.delete(url)

        # Check that the response status code is HTTP 204 No Content (deletion successful)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_delete_field_of_study(self):
        # Create a new custom user not associated with the course
        unauthorized_custom_user = CustomUser.objects.create_user(
            username="unauthorized", password="testpassword"
        )

        # Authenticate this unauthorized custom user
        self.client.force_authenticate(user=unauthorized_custom_user)

        # URL to delete the FieldOfStudy instance
        url = reverse("FieldOfStudy-delete", kwargs={"pk": self.field_of_study.pk})

        # send a DELETE request
        response = self.client.delete(url)

        # Check that the response status code is HTTP 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
