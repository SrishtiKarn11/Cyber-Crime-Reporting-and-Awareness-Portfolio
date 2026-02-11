from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from crimereporting.models import Complaint
from crimereporting.models import AwarenessPost

def home(request):
    return render(request, 'dashboard.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'users/register.html', {'form': form})

def awareness(request):
    posts = AwarenessPost.objects.all().order_by('-created_at')
    return render(request, 'users/awareness.html', {'posts': posts})

@login_required
def user_dashboard(request):
    return render(request, 'users/user_dashboard.html')

@login_required
def report_complaint(request):
    if request.method == 'POST':
        Complaint.objects.create(
            user=request.user,
            crime_type=request.POST.get('crime_type'),
            description=request.POST.get('description')
        )
        return redirect('/dashboard/')

    return render(request, 'users/report.html')

@login_required
def complaint_status(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'users/status.html', {'complaints': complaints})

