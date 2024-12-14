from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def user_dashboard(request):
    if request.user.groups.filter(name='Admin').exists():
        return render(request, 'admin_dashboard.html')
    elif request.user.groups.filter(name='Office Staff').exists():
        return render(request, 'staff_dashboard.html')
    elif request.user.groups.filter(name='Librarian').exists():
        return render(request, 'librarian_dashboard.html')
    return render(request, 'unauthorized.html')




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Student, LibraryHistory, FeesHistory

@login_required
@permission_required('auth.add_user', raise_exception=True)
def manage_staff(request):
    # Logic to manage Office Staff and Librarian accounts
    pass

@login_required
@permission_required('core.view_student', raise_exception=True)
def manage_students(request):
    students = Student.objects.all()
    return render(request, 'admin_students.html', {'students': students})

@login_required
@permission_required('core.view_feeshistory', raise_exception=True)
def manage_fees(request):
    fees = FeesHistory.objects.all()
    return render(request, 'admin_fees.html', {'fees': fees})

@login_required
@permission_required('core.view_libraryhistory', raise_exception=True)
def manage_library(request):
    library_records = LibraryHistory.objects.all()
    return render(request, 'admin_library.html', {'library_records': library_records})



@login_required
@permission_required('core.view_student', raise_exception=True)
def view_students(request):
    students = Student.objects.all()
    return render(request, 'office_students.html', {'students': students})

@login_required
@permission_required('core.add_feeshistory', raise_exception=True)
def add_fee(request):
    # Logic to add fees
    pass

@login_required
@permission_required('core.change_feeshistory', raise_exception=True)
def edit_fee(request, fee_id):
    fee = get_object_or_404(FeesHistory, id=fee_id)
    # Logic to edit fees
    pass



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Check the user's group
    if request.user.groups.filter(name="School Admin").exists():
        return render(request, 'admin_dashboard.html')
    elif request.user.groups.filter(name="Office Staff").exists():
        return render(request, 'office_dashboard.html')
    elif request.user.groups.filter(name="Librarian").exists():
        return render(request, 'librarian_dashboard.html')
    else:
        # Default fallback or access denied
        return redirect('login')


from django.conf import settings
from django.db import models

class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
