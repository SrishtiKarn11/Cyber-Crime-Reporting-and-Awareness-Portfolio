from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from crimereporting.models import Complaint
from django.shortcuts import get_object_or_404
from crimereporting.models import AwarenessPost

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin-panel/dashboard/')
        else:
            return render(request, 'adminpanel/login.html', {'error': 'Invalid admin credentials'})

    return render(request, 'adminpanel/login.html')

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

@user_passes_test(lambda u: u.is_staff)
def admin_complaints(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'adminpanel/complaints.html', {'complaints': complaints})


@user_passes_test(lambda u: u.is_staff)
def update_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)

    if request.method == 'POST':
        complaint.status = request.POST.get('status')
        complaint.save()
        return redirect('/admin-panel/complaints/')

    return render(request, 'adminpanel/update.html', {'complaint': complaint})


@user_passes_test(lambda u: u.is_staff)
def admin_awareness(request):
    if request.method == 'POST':
        AwarenessPost.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        return redirect('/admin-panel/awareness/')

    posts = AwarenessPost.objects.all().order_by('-created_at')
    return render(request, 'adminpanel/awareness.html', {'posts': posts})


