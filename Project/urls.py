from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("otherTables/", include("OtherTables.urls")),
    path("users/", include("Users.urls")),
    path("o/", include(oauth2_urls)),
]
