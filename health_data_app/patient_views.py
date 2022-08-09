from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from health_data_app.forms import *
from health_data_app.models import *
from PIL import Image
import stepic
from random import randrange
from .n_share import *

@login_required(login_url='login')
def patient_home(request):
    return render(request, 'patient/home_page.html')

@login_required(login_url='login')
def upload_report(request):
    if request.method == 'POST':
        form = UploadReport(request.POST, request.FILES)
        data = request.FILES['upload']
        print('hahah', data)
        fs = FileSystemStorage()
        file1 = fs.save(data.name, data)

        fileurl = fs.url(file1)
        import os
        print(os.getcwd())
        if form.is_valid():
            im = Image.open('mynew.jpg')

            form = form.save(commit=False)
            file = open('media/' + file1, "r+")
            file = file.read()
            os.remove('media/' + file1)
            print(file)

            file = bytes(file, 'utf-8')

            im1 = stepic.encode(im, file)
            irand = randrange(111, 99999999)
            filename = str(irand) + '.png'
            d = im1.save('media/crypto/' + filename, 'PNG')
            datapath = 'media/crypto/' + filename
            print(d)
            share1, share2 = generate_shares(datapath)
            form.rshare1 = share1
            form.rshare2 = share2
            form.report = 'crypto/' + filename

            form.patient = Patient.objects.get(login_id=request.user)
            form.save()
            pat = Patient.objects.get(login_id=request.user)
            pat.rshare1 = share1
            pat.save()
            messages.info(request, 'Report Uploaded Successfully')
            return redirect('upload_report')
    else:
        form = UploadReport()
    return render(request, 'patient/upload_report.html', {'form': form})

@login_required(login_url='login')
def report_request(request):
    patient = Patient.objects.get(login_id=request.user)
    report = Report.objects.filter(patient=patient)
    return render(request, 'patient/report_requests.html', {'reports': report})



@login_required(login_url='login')
def accept_doc_req(request, id):
    report = Report.objects.get(id=id)
    report.doctor_request = 2
    # data=report.doctor
    # data.rshare2=report.rshare2
    print(request.user)
    print(report.doctor)
    print(report.rshare2)
    pat = Patient.objects.get(login_id=request.user)
    drsharedata.objects.create(report_id=id, dr_userdata=pat, docterdata=report.doctor, dr_shareimage=report.rshare2)

    report.save()
    messages.info(request, 'Request for Viewing Report Accepted Successfully')
    return redirect('report_request')

@login_required(login_url='login')
def reject_doc_req(request, id):
    report = Report.objects.get(id=id)
    report.doctor_request = 3
    report.save()
    messages.info(request, 'Request for Viewing Report Rejected')
    return redirect('report_request')

@login_required(login_url='login')
def report_request_specialist(request):
    patient = Patient.objects.get(login_id=request.user)
    report = Report.objects.filter(patient=patient)
    return render(request, 'patient/report_requests_specialist.html', {'reports': report})

@login_required(login_url='login')
def accept_spe_req(request, id):
    report = Report.objects.get(id=id)
    report.specialist_request = 2
    #data=report.specialist
    #data.rshare2=report.rshare2
    pat = Patient.objects.get(login_id=request.user)

    spsharedata.objects.create(report_id=id, sp_userdata=pat, speciaisdata=report.specialist,
                               sp_shareimage=report.rshare2)
    report.save()
    messages.info(request, 'Request for Viewing Report Accepted Successfully')
    return redirect('report_request_specialist')

@login_required(login_url='login')
def reject_spe_req(request, id):
    report = Report.objects.get(id=id)
    report.doctor_request = 3
    report.save()
    messages.info(request, 'Request for Viewing Report Rejected')
    return redirect('report_request_specialist')

@login_required(login_url='login')
def complaint_register(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            data = Patient.objects.get(login_id=request.user)
            user.created_by = data

            user.save()
            messages.info(request, 'complaint Registered Successfully')
            return redirect('patient_home')
    else:
        form = ComplaintForm()
    return render(request, 'patient/comp_registation.html', {'complaint_register': form})

@login_required(login_url='login')
def Prescription_view(request):
    data = Patient.objects.get(login_id=request.user)
    pr = Prescription.objects.filter(patient=data)
    return render(request, 'patient/Prescription.html', {'Prescription': pr})

@login_required(login_url='login')
def complaint_view(request):
    print(id)
    # if request.method == 'POST':
    #     viewdata = request.POST.get('comp_view')
    #     data = Complaint.objects.get(id=id)
    #     data.comp_view = viewdata
    #     data.save()
    cr_user=request.user
    data = Patient.objects.get(login_id=cr_user)
    data = Complaint.objects.filter(created_by=data)


    return render(request, 'patient/comp_view.html',{'data':data})


@login_required(login_url='login')
def xray_upload(request):
    data=XrayForm()
    if request.method == 'POST':
        data=XrayForm(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect('patient_home')
    return render(request,'patient/xray_upload.html',{'data':data})

#
