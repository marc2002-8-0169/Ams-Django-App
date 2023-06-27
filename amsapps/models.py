from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.
class Assignment(models.Model):
    assignment_id = models.IntegerField(primary_key=True)
    assignment_name = models.CharField(max_length=50)
    instructor = models.ForeignKey('Instructor',on_delete=models.CASCADE)
    status = models.ForeignKey('Status',on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE)

    
    class Meta:
        managed = True
        db_table = 'assignment'

class Instructor(models.Model):
    instructor_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'instructor'

class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    id_number = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course}, {self.contact}, {self.address}, {self.gender}, {self.lastname}, {self.firstname}, {self.id_number}, {self.student_id},'
    
class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=50)
    
    class Meta:
        managed = True
        db_table = 'subject'

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    student_number = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'users'

class Status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)
    
    class Meta:
        managed = True
        db_table = 'status'



