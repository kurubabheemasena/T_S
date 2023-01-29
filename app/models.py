from django.db import models

# Create your models here.
class Teacher(models.Model):
    tnames=models.CharField(max_length=100)
    T_subject=models.CharField(max_length=100)
    deptno=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.tnames



class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    hiredate=models.DateField()
    address=models.CharField(max_length=100)
    deptno=models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname


