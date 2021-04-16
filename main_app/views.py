import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Story, Review
from .forms import ReviewForm, StoryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
def stories_create(request):
    if request.method == 'POST':
        cover_file = request.FILES.get('cover-file', None)
        form = StoryForm(request.POST)
        story = form.save(commit=False)
        if cover_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + \
                cover_file.name[cover_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(cover_file, os.environ['S3_BUCKET'], key)
                url = f"{os.environ['S3_BASE_URL']}{os.environ['S3_BUCKET']}/{key}"
                story.cover = url
            except:
                print('An error occurred uploading file to S3')
        story.user = request.user
        story.save()
        return redirect('detail', story_id=story.id)
    else:
        form = StoryForm()
        return render(request, 'main_app/story_form.html', {'form': form})


class StoryUpdate(UpdateView, LoginRequiredMixin):
    model = Story
    fields = ['title', 'author', 'genre', 'date', 'content', 'synopsis']

    def form_valid(self, form):
        cover_file = self.request.FILES.get('cover-file', None)
        form = StoryForm(self.request.POST)
        story = form.save(commit=False)
        if cover_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + \
                cover_file.name[cover_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(cover_file, os.environ['S3_BUCKET'], key)
                url = f"{os.environ['S3_BASE_URL']}{os.environ['S3_BUCKET']}/{key}"
                story.cover = url
            except:
                print('An error occurred uploading file to S3')
        story.user = self.request.user
        story.save()
        return super().form_valid(form)




# class StoryUpdate(UpdateView, LoginRequiredMixin):
#     model = Story
#     fields = ['title', 'author', 'genre', 'date', 'content', 'synopsis']


class StoryDelete(DeleteView, LoginRequiredMixin):
    model = Story
    success_url = '/stories/'


@login_required
def add_review(request, story_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.story_id = story_id
        new_review.save()
    return redirect('detail', story_id=story_id)


@login_required
def delete_review(request, story_id, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('detail', story_id=story_id)


class ReviewUpdate(UpdateView, LoginRequiredMixin):
    model = Review
    fields = ['content', 'rating']


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('stories_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
