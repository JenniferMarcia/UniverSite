from rest_framework import serializers
from .models import Course, FieldOfStudy


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course model"""

    class Meta:
        model = Course
        fields = "__all__"


class FieldOfStudySerializer(serializers.ModelSerializer):
    """Serializer for Field of study model"""

    class Meta:
        model = FieldOfStudy
        fields = "__all__"
