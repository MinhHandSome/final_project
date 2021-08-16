from django.db import models
from django.utils.translation import deactivate

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return "%s" % (self.name)
    class Meta:
        db_table ='Director'

class Genres(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return "%s" % (self.name)
    class Meta:
        db_table= 'Genres'

class Film(models.Model):
    title = models.CharField(max_length=50)
    image_url =models.CharField(max_length=250)
    video_url = models.CharField(max_length=250,default="")
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE
    )
    genres=models.ForeignKey(
        Genres,
        on_delete=models.CASCADE
    )
    actor = models.CharField(max_length=250,default="")
    runtime = models.IntegerField()
    rated = models.FloatField()
    content = models.TextField()
    # image = models.ImageField(null=True,blank=True,upload_to='images/')
    class Meta:
        db_table ="Flim"

