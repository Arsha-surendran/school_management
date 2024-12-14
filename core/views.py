from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from .models import Student, LibraryHistory, FeesHistory

@login_required
@permission_required('core.view_student', raise_exception=True)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def some_view(request):
    if not request.user.has_perm('core.view_student'):
        return redirect('unauthorized')  # Redirect to an unauthorized page

    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})



# Example for Office Staff (manage fees)
@login_required
@permission_required('core.view_feeshistory', raise_exception=True)
def fees_history_list(request):
    fees = FeesHistory.objects.all()
    return render(request, 'fees_history_list.html', {'fees': fees})



from django.shortcuts import get_object_or_404

@login_required
@permission_required('core.change_feeshistory', raise_exception=True)
def edit_fee_history(request, fee_id):
    fee = get_object_or_404(FeesHistory, id=fee_id)
    if request.method == 'POST':
        form = FeesHistoryForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fees_history_list')
    else:
        form = FeesHistoryForm(instance=fee)

    return render(request, 'edit_fee_history.html', {'form': form})


@login_required
@permission_required('core.delete_feeshistory', raise_exception=True)
def delete_fee_history(request, fee_id):
    fee = get_object_or_404(FeesHistory, id=fee_id)
    if request.method == 'POST':
        fee.delete()
        return redirect('fees_history_list')
    return render(request, 'confirm_delete_fee.html', {'fee': fee})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the desired page after login
    else:
        form = AuthenticationForm()

    return render(request, 'custom_login.html', {'form': form})




@login_required
def some_view(request):
    # Only logged-in users can access this view
    return render(request, 'some_template.html')



@login_required
def user_dashboard(request):
    if request.user.groups.filter(name='Admin').exists():
        return render(request, 'admin_dashboard.html')
    elif request.user.groups.filter(name='Office Staff').exists():
        return render(request, 'staff_dashboard.html')
    elif request.user.groups.filter(name='Librarian').exists():
        return render(request, 'librarian_dashboard.html')
    return render(request, 'unauthorized.html')


