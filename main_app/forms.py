from django.forms import ModelForm
from .models import Review, Story

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

class StoryForm(ModelForm):
    class Meta:
        model = Story
        exclude = ['user', 'cover']