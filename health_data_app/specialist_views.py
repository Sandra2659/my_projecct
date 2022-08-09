from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from PIL import Image
from health_data_app.forms import *
from health_data_app.models import *

@login_required(login_url='login')
def specialist_home(request):
    return render(request, 'specialist/home_page.html')

@login_required(login_url='login')
def profile(request):
    profile = Specialist.objects.filter(login_id=request.user)
    return render(request, 'specialist/profile2.html', {'profile': profile})

@login_required(login_url='login')
def update_profile2(request):
    profile = Specialist.objects.get(login_id=request.user)
    form = SpecialistRegister(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.info(request, 'Profile Updated Successfully')
        return redirect('profile2')
    return render(request, 'specialist/update_profile2.html', {'form': form})

@login_required(login_url='login')
def reports_shared_specialist(request):
    user = Specialist.objects.get(login_id=request.user)
    report = Report.objects.filter(patient__department=user.department)
    return render(request, 'specialist/reports_shared.html', {'reports': report})

@login_required(login_url='login')
def request_report(request, id):
    report = Report.objects.get(id=id)
    report.specialist = Specialist.objects.get(login_id=request.user)
    report.specialist_request = 1

    report.save()
    messages.info(request, 'Successfully send request to view report ')
    return redirect('reports_shared_specialist')

@login_required(login_url='login')
def accepted_requests_specialist(request):
    user = Specialist.objects.get(login_id=request.user)
    report = Report.objects.filter(specialist_request=2, patient__department=user.department, specialist=user)
    return render(request, 'specialist/accepted_requests.html', {'reports': report})

@login_required(login_url='login')
def sp_add_Prescription(request):

    if request.method == 'POST':
        form = PrescriptionForm(request.POST)

        if form.is_valid() :
            user = form.save(commit=False)

            user.save()
            messages.info(request, 'Add Prescription Successfully')
            return redirect('specialist_home')
    else:
        form = PrescriptionForm()
    return render(request, 'specialist/sp_add_Prescription.html', {'sp_add_Prescription': form})

@login_required(login_url='login')
def sp_refers_received(request):

    user = Specialist.objects.get(login_id=request.user)
    refer = Refer.objects.filter(referred_to=user)
    return render(request, 'specialist/sp_refers_received.html', {'refers': refer})