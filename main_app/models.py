from django.db import models
from django.urls import reverse 

GENRE = (
  ('SF', 'Sci-Fi'),
  ('FA', 'Fantasy'),
  ('HO', 'Horror'),
  ('NF', 'Non-Fiction'),
  ('MY', 'Mystery'),
  ('HU', 'Humour'),
  ('TH', 'Thriller'),
  ('CH', 'Children\'s'),
  ('HF', 'Historical Fiction'),
  ('SP', 'Spiritual'),
  ('RO', 'Romance'),
  ('ME', 'Memoir'),
  ('PO', 'Poetry'),
  ('WE', 'Western'),
  ('YA', 'Young Adult'),
)

RATING = (
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4', '4'),
  ('5', '5'),
)

# Create your models here.
class Story(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  user = models.CharField(max_length=50)
  genre = models.CharField(
    max_length=2,
    choices=GENRE,
    default=GENRE[0][0]
  )
  date = models.DateField()
  content = models.TextField()
  synopsis = models.TextField()
  cover = models.CharField(max_length=200,default="https://i.imgur.com/2WkT35M.jpg")

  def get_absolute_url(self):
    return reverse('detail', kwargs={'story_id': self.id})

  def __str__(self):
    return self.title

class Review(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  content = models.CharField(max_length=250)
  rating = models.CharField(
    max_length=1,
    choices=RATING,
    default=RATING[-1][-1]
  )

  story = models.ForeignKey(Story, on_delete=models.CASCADE)

  def __str__(self):
    return f"Content: {self.content}, Rating: {self.rating}"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'story_id': self.story.id})

  class Meta:
    ordering = ['-id']
