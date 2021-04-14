from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Story, Review
from .forms import ReviewForm

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stories_index(request):
    stories = Story.objects.all()
    for story in stories:
      print(story.genre)
    return render(request, 'stories/stories_index.html', {
            'stories': stories
    })

def stories_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    review_form = ReviewForm()
    return render(request, 'stories/detail.html', {
       'story': story,
       'review_form': review_form,
    })

class StoryCreate(CreateView):
    model = Story
    fields = '__all__'
    success_url = '/stories/'

class StoryUpdate(UpdateView):
    model = Story
    fields = '__all__'
    success_url = '/stories/'

class StoryDelete(DeleteView):
    model = Story
    success_url = '/stories/'

def add_review(request, story_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
      new_review = form.save(commit = False)
      new_review.story_id = story_id
      new_review.save()
    return redirect('detail', story_id=story_id)

def delete_review(request, story_id, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('detail', story_id=story_id)

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['content', 'rating']


