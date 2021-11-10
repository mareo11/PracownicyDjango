from django.db import models

class Studenci(models.Model):

   idStudent = models.CharField(max_length = 50)
   Imię = models.CharField(max_length = 50)
   Nazwisko = models.CharField(max_length = 50)
   Miasto = models.CharField(max_length = 50)
   Kod = models.CharField(max_length = 50)

   class Meta:
      db_table = "student"

