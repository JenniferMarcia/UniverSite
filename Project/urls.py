from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Django Applications urls
    path("otherTables/", include("OtherTables.urls")),
    path("users/", include("Users.urls")),
]
