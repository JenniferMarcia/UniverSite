from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Course, FieldOfStudy
from .serializers import CourseSerializer, FieldOfStudySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class CourseListView(generics.ListAPIView):
    """
    View for all Course objects.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific Course instance.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateView(generics.CreateAPIView):
    """
    View to create a new Course instance.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateView(generics.UpdateAPIView):
    """
    View to update an existing Course instance.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        TokenHasReadWriteScope,
    ]  # Only the user itself can update its own account
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        # get the Course instance to update
        Course = super().get_object()

        # Check if the current user is associated with this Course
        if not Course.custom_users.filter(pk=self.request.user.pk).exists():
            raise PermissionDenied("You are not authorized to update this Course.")

        return Course


class CourseDeleteView(generics.DestroyAPIView):
    """
    View to delete a Course instance.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        TokenHasReadWriteScope,
    ]  # Only the user itself can delete its own account
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        # Récupère l'instance de Course à supprimer
        Course = super().get_object()

        # Vérifie si l'utilisateur actuel est associé à ce Course
        if not Course.custom_users.filter(pk=self.request.user.pk).exists():
            raise PermissionDenied("You are not authorized to delete this Course")

        return Course


class FieldOfStudyListView(generics.ListAPIView):
    """
    View to retrieve all FieldOfStudy objects.
    """

    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer


class FieldOfStudyDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific FieldOfStudy instance.
    """

    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer


class FieldOfStudyCreateView(generics.CreateAPIView):
    """
    View to create a new FieldOfStudy instance.
    """

    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer


class FieldOfStudyUpdateView(generics.UpdateAPIView):
    """
    View to update an existing FieldOfStudy instance.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        TokenHasReadWriteScope,
    ]  # Only the user itself can delete its own account
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer

    def get_object(self):
        # Get the FieldOfStudy instance to update
        FieldOfStudy = super().get_object()

        # Check if the current user is associated with this FieldOfStudy
        if not FieldOfStudy.course.custom_users.filter(
            pk=self.request.user.pk
        ).exists():
            raise PermissionDenied("You are not authorized to update this FieldOfStudy")

        return FieldOfStudy


class FieldOfStudyDeleteView(generics.DestroyAPIView):
    """
    View to Delete a FieldOfStudy instance.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        TokenHasReadWriteScope,
    ]  # Only the user itself can delete its own account
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer

    def get_object(self):
        # Get the FieldOfStudy instance to delete
        FieldOfStudy = super().get_object()

        # Check if the current user is associated with this FieldOfStudy
        if not FieldOfStudy.course.custom_users.filter(
            pk=self.request.user.pk
        ).exists():
            raise PermissionDenied("You are not authorized to delete this FieldOfStudy")

        return FieldOfStudy
