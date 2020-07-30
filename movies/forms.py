from django import forms
from .models import Movie, Genre


class CreateMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created')


class CreateGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', )