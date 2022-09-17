from django.urls import path 
from .views import *

urlpatterns = [
    path('schools/', SchoolList.as_view(), name='school'),
    path('schools/<slug:abbreviation>', SchoolDetail.as_view(), name='school_detail'),
    path('departments/', DepartmentList.as_view(), name='department'),
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('lectures/', LectureAPIView.as_view(), name='lectures'),
    path('professors/', ProfessorAPIView.as_view(), name='professors'),
    path('courseofferings/', CourseOfferingAPIView.as_view(), name='courseofferings'),

    # Specific
    path('<slug:abbreviation>', SchoolDetail.as_view(), name='school_detail'),
    path('<slug:abbreviation>/<slug:dcode>', SchoolDepartment.as_view(), name='department_detail'),
    path('<slug:abbreviation>/<slug:dcode>/<slug:code>', SchoolDepartmentCourse.as_view(), name='course_detail'),
    path('<slug:abbreviation>/<slug:dcode>/<slug:code>/offerings', CourseOfferings.as_view(), name='course_offerings'),
    path('<slug:abbreviation>/<slug:dcode>/<slug:code>/<slug:term>', OfferingDetail.as_view(), name='offering_terms'),
    path('<slug:abbreviation>/<slug:dcode>/<slug:code>/<slug:term>/lectures', LectureList.as_view(), name='term_lectures'),

]