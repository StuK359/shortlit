from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stories/', views.stories_index, name='stories_index'),
    path('stories/<int:story_id>/', views.stories_detail, name="detail"),
    path('stories/create/', views.stories_create, name='stories_create'),
    path('stories/<int:pk>/update/', views.StoryUpdate.as_view(), name='stories_update'),
    path('stories/<int:pk>/delete/', views.StoryDelete.as_view(), name='stories_delete'),
    path('stories/<int:story_id>/add_review/', views.add_review, name='add_review'),
    path('stories/<int:story_id>/delete_review/<int:review_id>', views.delete_review, name='delete_review'),
    path('stories/<int:story_id>/update_review/<int:pk>', views.ReviewUpdate.as_view(), name='update_review'),
    path('stories/<int:story_id>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('favorites/', views.favorites_index, name="favorites_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path('user/', views.user_index, name='user_index'),
    path('author/<int:story_id>', views.author_index, name='author_index'),
]