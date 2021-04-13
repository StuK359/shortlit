from django.db import models
from django.urls import reverse 

# Create your models here.
class Story(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  user = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  date = models.DateField()
  content = models.TextField()
  synopsis = models.TextField()
  cover = models.TextField()


  def get_absolute_url(self):
    return reverse('detail', kwargs={'story_id': self.id})