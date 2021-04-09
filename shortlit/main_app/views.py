from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Story:
    def __init__(self, title, author, genre, date, synopsis):
        self.title = title
        self.author = author
        self.genre = genre
        self.date = date
        self.synopsis = synopsis

stories = [
    Story('Book of the Dead', 'Mr. Klingman IV', 'Horror', '04/09/2048', 'This book is about dead things'),
    Story('Book of the Dead', 'Mr. Klingman IV', 'Horror', '04/09/2048', 'This book is about dead things'),
    Story('Book of the Dead', 'Mr. Klingman IV', 'Horror', '04/09/2048', 'This book is about dead things'),
    Story('Book of the Dead', 'Mr. Klingman IV', 'Horror', '04/09/2048', 'This book is about dead things'),
]


# Define the home view
def home(request):
    return HttpResponse('<h1>BOOOOKS</h1>')

def about(request):
    return render(request, 'about.html')

def stories_index(request):
    return render(request, 'stories/stories_index.html', {
        'stories': stories
    })