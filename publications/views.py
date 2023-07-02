from django.shortcuts import render, get_object_or_404
from .models import Publication

def publications_list(request):
    publications = Publication.objects.all()
    context = {
        'publications': publications
    }
    return render(request, "publications_list.html", context)

def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    context = {
        'publication': publication
    }
    return render(request, "publication_detail.html", context)

