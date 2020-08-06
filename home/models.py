from django.db import models

# Create your models here.
class Create(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    class Meta:
        db_table="Create"