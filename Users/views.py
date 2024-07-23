from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserList(ListAPIView):
    """
    View to retrieve all Users.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserCreate(CreateAPIView):
    """
    View to register a new User.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(RetrieveAPIView):
    """
    View to retrieve an User .
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserUpdate(UpdateAPIView):
    """
    View to update an User .
    """

    permission_classes = [IsAuthenticated,]  # Only the user itself can update its information
    authentication_classes = [JWTAuthentication]

    def perform_update(self, serializer):
        if self.get_object().pk == self.request.user.pk:
            serializer.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDelete(DestroyAPIView):
    """
    View to Delete an User.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Only the user itself can delete its own account

    def perform_destroy(self, instance):
        if instance.pk == self.request.user.pk:  # Check if user deletes itsself
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UpdatePasswordView(APIView):
    """
    View to update user's password
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]  # Only authenticated users can update their password

    def post(self, request, *args, **kwargs):
        user = self.request.user  # Access authenticated user
        current_password = request.data["current_password"]
        new_password = request.data["new_password"]

        if not current_password or not new_password:
            return Response(
                {"error": "Current password and new password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.check_password(current_password):
            return Response(
                {"error": "Incorrect current password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()

        serializer = CustomUserSerializer(user)
        return Response(
            serializer.data if serializer else {}, status=status.HTTP_200_OK
        )


class LogoutView(APIView):
    """
    View for User logout with JWT token blacklisting.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]  # Only authenticated users can update password

    def post(self, request, *args, **kwargs):
        # Access the refresh token from request headers or cookies
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "User logout successfully"},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except (Exception.ObjectDoesNotExist, Exception.TokenError) as err:
            return Response({"message": str(err)}, status=status.HTTP_400_BAD_REQUEST)
