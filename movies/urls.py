from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('genres', views.genres, name="genres"),
]