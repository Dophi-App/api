from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    dcode = models.CharField(max_length=4)

    def __str__(self):
        return Department.code

class Course(models.Model):
    code = models.CharField(max_length=10)

    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    professor = models.CharField(max_length=50)

    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Lecture(models.Model):
    date = models.DateField()
    body = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
