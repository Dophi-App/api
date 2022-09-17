from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=50, default="none")

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    dcode = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Professor(models.Model):
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.department.dcode}{self.code}'

class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    FALL = 'fall'
    WINTER = 'winter'
    SPRING = 'spring'
    SUMMER = 'summer'

    TERM_CHOICES = [
        (FALL, 'fall'),
        (WINTER, 'winter'),
        (SPRING, 'spring'),
        (SUMMER, 'summer')
    ]

    term = models.CharField(max_length=15, default="mmmmyyyy")

    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.course} {self.term}'


class Lecture(models.Model):
    number = models.IntegerField(default=0)
    date = models.DateField()
    body = models.TextField(blank=True, null=True)
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.date} Lecture'
