from django.shortcuts import render
from .models import Movies
from django.views.generic.list import ListView
from django.core.paginator import Paginator     #Pagination for normal Views

# Create your views here.
class MoviesList(ListView):
    model = Movies
    template_name = 'movies.html'
    context_object_name = 'movies_list'
    paginate_by = 3     # Pagination for Class Based View

def movies_list(request):
    movies_objects = Movies.objects.all()
    
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movies_objects = movies_objects.filter(name__icontains=movie_name)

    paginate = Paginator(movies_objects, 3)

    page = request.GET.get('page')
    movies_objects = paginate.get_page(page)
    
    return render(request, 'movies.html', {
        'movies_object': movies_objects,
        
    })
