from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return render(request, 'service_requests/request_submitted.html')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/track_request.html', {'requests': requests})

def home(request):
    """the homepage for gas utility services"""
    return render(request, 'service_requests/home.html')

def request_submitted(request):
    
    return render(request, 'service_requests/request_submitted.html')
    
