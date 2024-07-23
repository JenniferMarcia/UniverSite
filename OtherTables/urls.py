from django.urls import path
from .views import (
    CourseCreateView,
    CourseDeleteView,
    CourseDetailView,
    CourseListView,
    CourseUpdateView,
    FieldOfStudyCreateView,
    FieldOfStudyDeleteView,
    FieldOfStudyDetailView,
    FieldOfStudyListView,
    FieldOfStudyUpdateView,
)


urlpatterns = [
    # CRUD course urls
    path("course/", CourseListView.as_view(), name="Course-list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="Course-detail"),
    path("course/create/", CourseCreateView.as_view(), name="Course-create"),
    path("course/update/<int:pk>/", CourseUpdateView.as_view(), name="Course-update"),
    path("course/delete/<int:pk>/", CourseDeleteView.as_view(), name="Course-delete"),
    # CRUD fieldOfStudy urls
    path("fieldOfStudy/", FieldOfStudyListView.as_view(), name="FieldOfStudy-list"),
    path("fieldOfStudy/<int:pk>/", FieldOfStudyDetailView.as_view(), name="FieldOfStudy-detail"),
    path("fieldOfStudy/create/",FieldOfStudyCreateView.as_view(), name="FieldOfStudy-create"),
    path("fieldOfStudy/update/<int:pk>/",FieldOfStudyUpdateView.as_view(),name="FieldOfStudy-update"),
    path("fieldOfStudy/delete/<int:pk>/",FieldOfStudyDeleteView.as_view(),name="FieldOfStudy-delete",),
]
