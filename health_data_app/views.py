from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from health_data_app.forms import LoginRegister, DoctorRegister, SpecialistRegister, PatientRegister
from .models import *
from PIL import Image
import stepic
from .n_share import *



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('ca_home')
            elif user.is_doctor:
                return redirect('doctor_home')
            elif user.is_specialist:
                return redirect('specialist_home')
            elif user.is_patient:
                return redirect('patient_home')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'registration/login.html')


def home(request):
    return render(request,'index.html')

def login_page(request):
    return redirect('login')


# def login_view(request):
#     user1 = request.user
#     if user1 is not None:
#         # login(request, user)
#         if user1.is_staff:
#             return redirect('ca_home')
#         elif user1.is_doctor:
#             return redirect('doctor_home')
#         elif user1.is_specialist:
#             return redirect('specialist_home')
#         elif user1.is_patient:
#             return redirect('patient_home')
#     else:
#         messages.info(request, 'Invalid Credentials')




def doctor_register(request):
    login_form = LoginRegister()
    doctor_form = DoctorRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        doctor_form = DoctorRegister(request.POST, request.FILES)
        if login_form.is_valid() and doctor_form.is_valid():
            user = login_form.save(commit=False)
            user.is_doctor = True
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.login_id = user
            doctor.save()
            messages.info(request, 'Doctor Registered Successfully')
            return redirect('login_page')
    return render(request, 'doctor_register.html', {'login_form': login_form, 'doctor_form': doctor_form})


def specialist_register(request):
    login_form = LoginRegister()
    specialist_form = SpecialistRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        specialist_form = SpecialistRegister(request.POST, request.FILES)
        if login_form.is_valid() and specialist_form.is_valid():
            user = login_form.save(commit=False)
            user.is_specialist = True
            user.save()
            specialist = specialist_form.save(commit=False)
            specialist.login_id = user
            specialist.save()
            messages.info(request, 'Specialist Registered Successfully')
            return redirect('login_page')
    return render(request, 'specialist_register.html', {'login_form': login_form, 'specialist_form': specialist_form})

def patient_register(request):
    login_form = LoginRegister()
    patient_form = PatientRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        patient_form = PatientRegister(request.POST, request.FILES)
        if login_form.is_valid() and patient_form.is_valid():
            user = login_form.save(commit=False)
            user.is_patient = True
            user.save()
            patient = patient_form.save(commit=False)
            patient.login_id = user
            patient.save()
            messages.info(request, 'Patient Registered Successfully')
            return redirect('login_page')
    return render(request, 'patient_register.html', {'login_form': login_form, 'patient_form': patient_form})


def logout_view(request):
    logout(request)
    return redirect('login_view')

def decrypt(request,id=None):
    data=Report.objects.get(id=id)
    #pdata=Patient.objects.get(login_id=data)
    print(request.user)

    try:
        dr_data=Doctor.objects.get(login_id=request.user)
        data2=drsharedata.objects.get(report_id=id,dr_userdata=data.patient,docterdata=dr_data)
        compress_shares(data.rshare1,data2.dr_shareimage)
        #im2 = Image.open(data.report)
        im2 = Image.open('media/crypto/compress.png')
        stegoImage = stepic.decode(im2)
        print('haha',stegoImage)
        messages.info(request, stegoImage)

        #return redirect('accepted_requests')
        return render(request,'dataview.html',{'data':stegoImage})
    except:
        sp_data=Specialist.objects.get(login_id=request.user)
        data2=spsharedata.objects.get(report_id=id,sp_userdata=data.patient,speciaisdata=sp_data)
        compress_shares(data.rshare1,data2.sp_shareimage)
        im2 = Image.open('media/crypto/compress.png')
        stegoImage = stepic.decode(im2)
        print('haha',stegoImage)
        messages.info(request, stegoImage)
        #return redirect('accepted_requests')
        return render(request,'spdataview.html',{'data':stegoImage})

    # for data in data:
    #     print(data.report)
    #     d=data.report


