import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "John Doe"  # Change as needed
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

print("-" * 40)


library_name = "Central Library"  # Change as needed
try:
    library = Library.objects.get(name=library_name)
    books_in_library = Book.objects.filter(library=library)
    print(f"Books in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

print("-" * 40)


try:
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library {library_name}")
