# Django Permissions & Groups Setup

## Custom Permissions:
- can_view: View articles.
- can_create: Create new articles.
- can_edit: Edit existing articles.
- can_delete: Delete articles.

## User Groups:
- **Viewers**: Can only view articles.
- **Editors**: Can view, create, and edit articles.
- **Admins**: Full access.

## How to Assign Groups:
1. Open Django Admin Panel.
2. Navigate to Users → Select User.
3. Assign to Viewers, Editors, or Admins.

## Testing:
- Log in with different users to verify restricted access.
