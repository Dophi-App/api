from rest_framework import serializers
from course.models import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'abbreviation')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'dcode')

class CourseSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Course
        fields = ('code', 'name')

class LectureSerializer(serializers.ModelSerializer):
    offering = serializers.CharField(source='offering.__str__')
    class Meta:
        model = Lecture
        fields = ('date', 'body', 'offering')

class CourseOfferingSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.__str__')
    professor = serializers.CharField(source='professor.__str__')
    class Meta:
        model = CourseOffering
        fields = ('course', 'term', 'professor')

class ProfessorSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')
    class Meta:
        model = Professor
        fields = ('first_name', 'last_name', 'department')