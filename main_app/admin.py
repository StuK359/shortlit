from django.contrib import admin
from .models import Story, Review, Favorite

# Register your models here.
admin.site.register(Story)
admin.site.register(Review)
admin.site.register(Favorite)