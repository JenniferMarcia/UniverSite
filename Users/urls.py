from django.urls import include, path
from .views import (
    CustomUserList,
    CustomUserCreate,
    CustomUserDelete,
    CustomUserDetail,
    CustomUserUpdate,
    UpdatePasswordView,
    LogoutView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # CRUD User urls
    path("", CustomUserList.as_view(), name="user-list"),
    path("<int:pk>/", CustomUserDetail.as_view(), name="user-detail"),
    path("<int:pk>/update/", CustomUserUpdate.as_view(), name="user-update"),
    path("create/", CustomUserCreate.as_view(), name="user-create"),
    path("<int:pk>/delete/", CustomUserDelete.as_view(), name="user-delete"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "update-password/<int:pk>/",
        UpdatePasswordView.as_view(),
        name="update-password",
    ),
    # JWT urls
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"), 
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), 
]
