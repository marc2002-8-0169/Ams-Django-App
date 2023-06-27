from django.db import models

class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    id_number = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'student'