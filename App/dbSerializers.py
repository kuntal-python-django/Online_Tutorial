from rest_framework import serializers
from .models import *


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ['title', 'author', 'tag', 'question', 'solution']