from django.db import models
import json

from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.

class Hifdh_Table(models.Model):

    teacher_name_choices = [('Israr', 'Israr'), ('Qari Abdul Azeem', 'Qari Abdul Azeem')]

    student_names = models.ForeignKey('Student_Names', default='', on_delete=models.CASCADE)
    surah = models.CharField(max_length=500)
    ayah_start = models.IntegerField()
    ayah_end = models.IntegerField()
    mistakes = models.IntegerField()
    stuck = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    teacher = models.CharField(max_length=500, choices=teacher_name_choices, default='Qari Abdul Azeem')


class Student_Names(models.Model):

    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
