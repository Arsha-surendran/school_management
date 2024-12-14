from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Student, LibraryHistory, FeesHistory

# Create groups
admin_group, _ = Group.objects.get_or_create(name='School Admin')
office_staff_group, _ = Group.objects.get_or_create(name='Office Staff')
librarian_group, _ = Group.objects.get_or_create(name='Librarian')

# Assign permissions to groups
student_ct = ContentType.objects.get_for_model(Student)
library_ct = ContentType.objects.get_for_model(LibraryHistory)
fees_ct = ContentType.objects.get_for_model(FeesHistory)

# Admin Permissions
admin_permissions = Permission.objects.filter(content_type__in=[student_ct, library_ct, fees_ct])
admin_group.permissions.set(admin_permissions)

# Office Staff Permissions
office_staff_permissions = Permission.objects.filter(content_type=student_ct) | \
                           Permission.objects.filter(content_type=fees_ct)
office_staff_group.permissions.set(office_staff_permissions)

# Librarian Permissions
librarian_permissions = Permission.objects.filter(content_type=student_ct, codename__startswith='view') | \
                        Permission.objects.filter(content_type=library_ct, codename__startswith='view')
librarian_group.permissions.set(librarian_permissions)
