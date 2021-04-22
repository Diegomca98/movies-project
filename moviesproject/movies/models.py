from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    rating = models.FloatField(verbose_name="Rating")

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    
    def __str__(self):
        return self.name
    

