from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255,default='')
    biography = models.TextField()
    birth = models.DateField()
    death = models.DateField(null=True,blank=True)
    nationality = models.CharField(max_length=255)
    awards = models.TextField()

    def __str__(self):
        return self.name