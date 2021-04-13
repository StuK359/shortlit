from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Story

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stories_index(request):
    stories = Story.objects.all()
    return render(request, 'stories/stories_index.html', {
            'stories': stories
    })

def stories_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'stories/detail.html', {
        'story': story
    })

class StoryCreate(CreateView):
    model = Story
    fields = '__all__'
    success_url = '/stories/'

class StoryUpdate(UpdateView):
    model = Story
    fields = '__all__'
    success_url = '/stories/'