from django.db import models


class Course(models.Model):
    """
    Course model
    """

    custom_users = models.ManyToManyField(
        "Users.CustomUser", verbose_name=("Universities")
    )
    course_name = models.CharField(max_length=100)
    prerequisites = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.course_name


class FieldOfStudy(models.Model):
    """
    FieldOfStudy model

    """

    field_name = models.CharField(max_length=30, unique=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.field_name
