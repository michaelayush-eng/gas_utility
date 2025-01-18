from django.shortcuts import render, get_object_or_404, redirect
from service_requests.models import ServiceRequest
from support.forms import UpdateRequestForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'support/manage_requests.html', {'requests': requests})

@staff_member_required
def update_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = UpdateRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('manage_requests')  # Redirect to the list of requests after updating
    else:
        form = UpdateRequestForm(instance=service_request)
    return render(request, 'support/update_request.html', {'form': form, 'service_request': service_request})
