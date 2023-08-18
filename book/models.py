from django.db import models
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField("author.Author")
    image = models.ImageField(upload_to="uploads/book/images/")
    description = models.TextField()
    category = models.ManyToManyField("Category")

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name