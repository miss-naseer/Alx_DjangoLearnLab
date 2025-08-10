# Django Permissions & Groups Setup

## Overview
This Django project uses custom permissions and groups to control access to `Book` model actions:

- **can_view** – View the list of books
- **can_create** – Add a new book
- **can_edit** – Edit existing books
- **can_delete** – Remove books

Permissions are assigned to groups, and views are protected using `@permission_required`.

---

## 1. Custom Permissions
Defined in `bookshelf/models.py`:

```python
class Book(models.Model):
    # fields...
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
