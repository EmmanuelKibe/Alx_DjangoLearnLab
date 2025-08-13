import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Books, Library, Librarian

# create a shortcut so we can use books.all()
books = Books.objects

# 1️⃣ Query all books by a specific author
author_name = "John Doe"  # change as needed
books_by_author = books.all().filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")
print("-" * 40)

# 2️⃣ List all books in a library
library_name = "Central Library"  # change as needed
books_in_library = books.all().filter(library__name=library_name)
print(f"Books in {library_name}:")
for book in books_in_library:
    print(f"- {book.title}")
print("-" * 40)

# 3️⃣ Retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")

