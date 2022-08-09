from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from health_data_app.forms import *
from health_data_app.models import *

@login_required(login_url='login')
def doctor_home(request):
    return render(request, 'doctor/home_page.html')

@login_required(login_url='login')
def reports_shared(request):
    user = Doctor.objects.get(login_id=request.user)
    report = Report.objects.filter(patient__department=user.department)
    return render(request, 'doctor/reports_shared.html', {'reports': report})

# @login_required(login_url='login')
def request_report_view(request, id):
    report = Report.objects.get(id=id)
    report.doctor = Doctor.objects.get(login_id=request.user)
    report.doctor_request = 1
    report.save()
    messages.info(request, 'Successfully send request to view report ')
    return redirect('reports_shared')

@login_required(login_url='login')
def accepted_requests(request):
    user = Doctor.objects.get(login_id=request.user)
    report = Report.objects.filter(doctor_request=2, patient__department=user.department, doctor=user)
    return render(request, 'doctor/accepted_requests.html', {'reports': report})

@login_required(login_url='login')
def refer_patient(request):
    if request.method == 'POST':
        form = ReferForm(request.POST)
        if form.is_valid():
            refer = form.save(commit=False)
            refer.referred_by = Doctor.objects.get(login_id=request.user)
            refer.save()
            messages.info(request, 'Refered Patient Successfully')
            return redirect('refer_patient')
    else:
        form = ReferForm()
    return render(request, 'doctor/refer_patient.html', {'form': form})

@login_required(login_url='login')
def refers_received(request):
    user = Doctor.objects.get(login_id=request.user)
    refer = Refer.objects.filter(referred_to=user)
    return render(request, 'doctor/refers_received.html', {'refers': refer})

@login_required(login_url='login')
def dr_add_Prescription(request):

    if request.method == 'POST':
        form = PrescriptionForm(request.POST)

        if form.is_valid() :
            user = form.save(commit=False)

            user.save()
            messages.info(request, 'Add Prescription Successfully')
            return redirect('doctor_home')
    else:
        form = PrescriptionForm()
    return render(request, 'doctor/dr_add_Prescription.html', {'dr_add_Prescription': form})

@login_required(login_url='login')
def profile(request):
    profile = Doctor.objects.filter(login_id=request.user)
    return render(request, 'doctor/profile1.html', {'profile': profile})

@login_required(login_url='login')
def update_profile(request):
    profile = Doctor.objects.get(login_id=request.user)
    form = DoctorRegister(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.info(request, 'Profile Updated Successfully')
        return redirect('profile1')
    return render(request, 'doctor/update_profile1.html', {'form': form})

def drview(request):
    # user = Doctor.objects.get(user=request.user)
    u = request.user
    xray = drsharereport.objects.filter(doctor__login_id=u)
    return render(request,'doctor/xrayview.html',{'xray':xray})