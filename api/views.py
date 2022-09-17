from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from course.models import *
from .serializers import *

# SCHOOL 
class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetail(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'abbreviation'

class SchoolDepartment(generics.RetrieveAPIView):
    serializer_class = DepartmentSerializer
    lookup_field = 'dcode'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        
        queryset = Department.objects.filter(school__abbreviation=school)
        return queryset

class SchoolDepartmentCourse(generics.RetrieveAPIView):
    model = Course
    serializer_class = CourseSerializer
    lookup_field = 'code'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        
        queryset = Course.objects.filter(department__dcode=dept, 
            department__school__abbreviation=school)
        return queryset

class CourseOfferings(generics.ListAPIView):
    """
    Get the offerings for a particular course
    """
    serializer_class = CourseOfferingSerializer
    lookup_field = 'code'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        course = self.kwargs['code']
        
        queryset = CourseOffering.objects.filter(
            course__code=course,
            course__department__dcode=dept, 
            course__department__school__abbreviation=school)
        return queryset

class OfferingDetail(generics.RetrieveAPIView):
    serializer_class = CourseOfferingSerializer
    lookup_field = 'term'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        course = self.kwargs['code']
        
        queryset = CourseOffering.objects.filter(
            course__code=course,
            course__department__dcode=dept, 
            course__department__school__abbreviation=school)
        return queryset

class LectureList(generics.ListAPIView):
    serializer_class = LectureSerializer
    lookup_field = 'date'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        course = self.kwargs['code']
        offering = self.kwargs['term']
        
        queryset = Lecture.objects.filter(
            offering__term=offering,
            offering__course__code=course,
            offering__course__department__dcode=dept, 
            offering__course__department__school__abbreviation=school)
        return queryset

class LectureDetail(generics.RetrieveAPIView):
    serializer_class = LectureSerializer
    lookup_field = 'number'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        course = self.kwargs['code']
        offering = self.kwargs['term']
        
        queryset = Lecture.objects.filter(
            offering__term=offering,
            offering__course__code=course,
            offering__course__department__dcode=dept, 
            offering__course__department__school__abbreviation=school)
        return queryset

class LectureRUD(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = LectureUpdateSerializer
    lookup_field = 'number'

    def get_queryset(self):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        course = self.kwargs['code']
        offering = self.kwargs['term']
        
        queryset = Lecture.objects.filter(
            offering__term=offering,
            offering__course__code=course,
            offering__course__department__dcode=dept, 
            offering__course__department__school__abbreviation=school)
        return queryset
    
class LectureCreate(generics.CreateAPIView): 
    serializer_class = LectureCreateSerializer
    # def get_queryset(self):
    #     school = self.kwargs['abbreviation']
    #     dept = self.kwargs['dcode']
    #     course = self.kwargs['code']
    #     offering = self.kwargs['term']
        
    #     queryset = Lecture.objects.filter(
    #         offering__term=offering,
    #         offering__course__code=course,
    #         offering__course__department__dcode=dept, 
    #         offering__course__department__school__abbreviation=school)
    #     return queryset
    
    def post(self, request, *args, **kwargs):
        school = self.kwargs['abbreviation']
        dept = self.kwargs['dcode']
        course = self.kwargs['code']
        term = self.kwargs['term']

        offering = get_object_or_404(CourseOffering, term=term, 
            course__code=course, 
            course__department__dcode=dept,
            course__department__school__abbreviation=school)
        


        return self.create(request, *args, **kwargs)


# DEPARTMENT
class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# COURSE
class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LectureAPIView(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class ProfessorAPIView(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CourseOfferingAPIView(generics.ListAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer
