from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    totalStudents = models.IntegerField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    busId = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    cost = models.IntegerField()

    def __int__(self):
        return self.busId

gender_choose = (
    ("male","Male"),
    ("female","Female"),
    ("others", "Others")
)

class Student(models.Model):
    studentId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choose)
    department = models.ForeignKey('Department',on_delete=models.CASCADE)
    bus = models.ForeignKey('Bus',on_delete=models.CASCADE, default=1001)

    def __str__(self):
        return self.name
