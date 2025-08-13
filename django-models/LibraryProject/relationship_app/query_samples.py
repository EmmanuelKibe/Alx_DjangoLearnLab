import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"  
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

print("-" * 40)

#List all books in a library
library_name = "Central Library"  # Change as needed
books_in_library = Book.all().filter(library__name=library_name)
print(f"Books in {library_name}:")
for book in books_in_library:
    print(f"- {book.title}")
print("-" * 40)

#Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library {library_name}")
