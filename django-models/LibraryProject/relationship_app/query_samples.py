import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Books, Library, Librarian

# Using lowercase books variable
books = Books.objects

# Query all books by a specific author
author_name = "John Doe"
books_by_author = books.all().filter(author__name=author_name)  # <- contains books.all()
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <- exact string match
books_in_library = books.all().filter(library=library)  # <- contains books.all()
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(librarian.name)


