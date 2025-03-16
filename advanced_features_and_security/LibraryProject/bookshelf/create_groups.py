from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Article

class Command(BaseCommand):
    help = "Create default user groups with permissions"

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Article)

        # Define groups
        groups = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, permissions in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.get(codename=perm, content_type=content_type)
                group.permissions.add(permission)
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' created/updated successfully!"))
