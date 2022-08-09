from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from health_data_app.models import *

@login_required(login_url='login')
def ca_home(request):
    return render(request, 'central_authority/home_page.html')


@login_required(login_url='login')
def patient_registration(request):
    patient = Patient.objects.filter(verified=False)
    return render(request, 'central_authority/patient_registration.html', {'patients': patient})


@login_required(login_url='login')
def verify_patient(request, login_id_id):
    pat = Patient.objects.get(login_id=login_id_id)
    pat.verified = True
    pat.save()
    messages.info(request, 'Patient Verified Successfully')
    return redirect('patient_registration')

@login_required(login_url='login')
def doctor_registration(request):
    doc = Doctor.objects.filter(verified=False)
    return render(request, 'central_authority/doctor_registration.html', {'doctors': doc})

@login_required(login_url='login')
def verify_doctor(request, login_id_id):
    doc = Doctor.objects.get(login_id=login_id_id)
    doc.verified = True
    doc.save()
    messages.info(request, 'Doctor Verified Successfully')
    return redirect('doctor_registration')

@login_required(login_url='login')
def specialist_registration(request):
    s = Specialist.objects.filter(verified=False)
    return render(request, 'central_authority/specialist_registration.html', {'specialist': s})

@login_required(login_url='login')
def verify_specialist(request, login_id_id):
    s = Specialist.objects.get(login_id=login_id_id)
    s.verified = True
    s.save()
    messages.info(request, 'Patient Verified Successfully')
    return redirect('specialist_registration')

@login_required(login_url='login')
def patients(request):
    patient = Patient.objects.filter(verified=True)
    return render(request, 'central_authority/patient.html', {'patients': patient})

@login_required(login_url='login')
def patient_delete(request, login_id_id):
    p = Login.objects.get(id=login_id_id)
    p.delete()
    messages.info(request, 'Patient Deleted')
    return redirect('patients')

@login_required(login_url='login')
def doctor(request):
    doc = Doctor.objects.filter(verified=True)
    return render(request, 'central_authority/doctor.html', {'doctors': doc})

@login_required(login_url='login')
def doctor_delete(request, login_id_id):
    doc = Login.objects.get(id=login_id_id)
    doc.delete()
    messages.info(request, 'Doctor Deleted')
    return redirect('doctor')

@login_required(login_url='login')
def specialist(request):
    s = Specialist.objects.filter(verified=True)
    return render(request, 'central_authority/specialist.html', {'specialist': s})

@login_required(login_url='login')
def specialist_delete(request, login_id_id):
    p = Login.objects.get(id=login_id_id)
    p.delete()
    messages.info(request, 'Specialist Deleted')
    return redirect('specialist')
@login_required(login_url='login')
def complaint_view(request):
    c = Complaint.objects.all()

    return render(request, 'central_authority/complaint.html', {'Complaint': c})

@login_required(login_url='login')
def replayview(request,id=None):
    print(id)
    if request.method =='POST':
        replaydata = request.POST.get('replay')
        data = Complaint.objects.get(id=id)
        data.replay = replaydata
        data.save()
        return redirect('complaint_view')
    return render(request, 'central_authority/replay.html')

