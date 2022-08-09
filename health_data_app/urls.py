from django.contrib import admin
from django.urls import path

from health_data_app import views, ca_views, doctor_views, patient_views, specialist_views
urlpatterns = [
    path('',views.home,name='home'),
    path('login_page', views.login_page, name='login_page'),
    path('login_view', views.login_view, name='login_view'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('specialist_register/', views.specialist_register, name='specialist_register'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('ca_home/', ca_views.ca_home, name='ca_home'),
    path('patient_registration/', ca_views.patient_registration, name='patient_registration'),
    path('doctor_registration/', ca_views.doctor_registration, name='doctor_registration'),
    path('specialist_registration/', ca_views.specialist_registration, name='specialist_registration'),
    path('verify_patient/<int:login_id_id>/', ca_views.verify_patient, name='verify_patient'),
    path('verify_doctor/<int:login_id_id>/', ca_views.verify_doctor, name='verify_doctor'),
    path('verify_specialist/<int:login_id_id>/', ca_views.verify_specialist, name='verify_specialist'),
    path('patients/', ca_views.patients, name='patients'),
    path('patient_delete/<int:login_id_id>/', ca_views.patient_delete, name='patient_delete'),
    path('doctor/', ca_views.doctor, name='doctor'),
    path('doctor_delete/<int:login_id_id>/', ca_views.doctor_delete, name='doctor_delete'),
    path('specialist/', ca_views.specialist, name='specialist'),
    path('specialist_delete/<int:login_id_id>/', ca_views.specialist_delete, name='specialist_delete'),
    path('complaint_view', ca_views.complaint_view, name='complaint_view'),
    path('replay/<int:id>/', ca_views.replayview, name='replay'),

    path('doctor_home/', doctor_views.doctor_home, name='doctor_home'),
    path('reports_shared/', doctor_views.reports_shared, name='reports_shared'),
    path('request_report_view/<int:id>/', doctor_views.request_report_view, name='request_report_view'),
    path('accepted_requests/', doctor_views.accepted_requests, name='accepted_requests'),
    path('refer_patient/', doctor_views.refer_patient, name='refer_patient'),
    path('refers_received/', doctor_views.refers_received, name='refers_received'),
    path('dr_add_Prescription/', doctor_views.dr_add_Prescription, name='dr_add_Prescription'),
    path('profile1/', doctor_views.profile, name='profile1'),
    path('update_profile1/', doctor_views.update_profile, name='update_profile1'),
    path('drview',doctor_views.drview,name='drview'),



    path('patient_home/', patient_views.patient_home, name='patient_home'),
    path('upload_report/', patient_views.upload_report, name='upload_report'),
    path('report_request/', patient_views.report_request, name='report_request'),
    path('accept_doc_req/<int:id>/', patient_views.accept_doc_req, name='accept_doc_req'),
    path('reject_doc_req/<int:id>/', patient_views.reject_doc_req, name='reject_doc_req'),
    path('report_request_specialist/', patient_views.report_request_specialist, name='report_request_specialist'),
    path('accept_spe_req/<int:id>/', patient_views.accept_spe_req, name='accept_spe_req'),
    path('reject_spe_req/<int:id>/', patient_views.reject_spe_req, name='reject_spe_req'),
    path('complaint_register/', patient_views.complaint_register, name='complaint_register'),
    path('Prescription_view/', patient_views.Prescription_view, name='Prescription_view'),
    path('comp_view', patient_views.complaint_view, name='comp_view'),
    path('xray_upload', patient_views.xray_upload, name='xray_upload'),

    path('specialist_home/', specialist_views.specialist_home, name='specialist_home'),
    path('profile2/', specialist_views.profile, name='profile2'),
    path('sp_refers_received/', specialist_views.sp_refers_received, name='sp_refers_received'),
    path('update_profile2/', specialist_views.update_profile2, name='update_profile2'),
    path('reports_shared_specialist/', specialist_views.reports_shared_specialist, name='reports_shared_specialist'),
    path('request_report/<int:id>/', specialist_views.request_report, name='request_report'),
    path('accepted_requests_specialist/', specialist_views.accepted_requests_specialist, name='accepted_requests_specialist'),
    path('sp_add_Prescription/', specialist_views.sp_add_Prescription, name='sp_add_Prescription'),
    path('decrypt/<int:id>/', views.decrypt, name='decrypt'),


]
