from django.urls import path
from . import views

urlpatterns = [
    path('v1/longest-duration-movies/', views.loang_duration_movies, name = 'longest-duration-movies'),
    path('v1/new-movie/', views.new_movies, name = 'new-movie'),
    path('v1/top-rated-movies/', views.top_rated_movies, name = 'top_rated_movies'),

]