# Advanced API Project

This Django project demonstrates advanced API development using Django REST Framework (DRF) with custom and generic views for the `Book` model.

## View Configurations

1. **BookListView** (`GET /api/books/`):
   - Generic: `ListAPIView`
   - Purpose: Lists all books, with optional `year` filter (e.g., `/api/books/?year=2000`).
   - Permissions: Public (read-only).

2. **BookDetailView** (`GET /api/books/<pk>/`):
   - Generic: `RetrieveAPIView`
   - Purpose: Retrieves a single book by ID.
   - Permissions: Public (read-only).

3. **BookCreateView** (`POST /api/books/create/`):
   - Generic: `CreateAPIView`
   - Purpose: Creates a new book.
   - Custom: Logs creation event.
   - Permissions: Authenticated users only.

4. **BookUpdateView** (`PUT /api/books/<pk>/update/`):
   - Generic: `UpdateAPIView`
   - Purpose: Updates an existing book.
   - Custom: Validates non-empty title.
   - Permissions: Authenticated users only.

5. **BookDeleteView** (`DELETE /api/books/<pk>/delete/`):
   - Generic: `DestroyAPIView`
   - Purpose: Deletes a book.
   - Permissions: Authenticated users only.

## Setup
1. Run `python3 manage.py migrate` to set up the database.
2. Create a superuser with `python3 manage.py createsuperuser`.
3. Start the server: `python3 manage.py runserver`.

## Testing
Use `curl` or Postman to test endpoints (see Step 5 in the task description).
