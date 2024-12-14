from django.shortcuts import render

# Create your views here.
@login_required
@permission_required('core.view_libraryhistory', raise_exception=True)
def view_library_history(request):
    library_records = LibraryHistory.objects.all()
    return render(request, 'librarian_library.html', {'library_records': library_records})

@login_required
@permission_required('core.view_student', raise_exception=True)
def view_students(request):
    students = Student.objects.all()
    return render(request, 'librarian_students.html', {'students': students})
