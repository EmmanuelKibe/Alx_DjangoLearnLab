from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book

# Function-based view — lists all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view — shows details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # books.all() comes from related_name='books' in the Book model
        context['books'] = self.object.books.all()
        return context

