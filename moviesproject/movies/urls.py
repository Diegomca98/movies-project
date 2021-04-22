from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name="movies"),
    #path('', views.MoviesList.as_view(), name="movies"),
]
