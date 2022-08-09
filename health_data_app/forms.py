import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from health_data_app.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

DEPARTMENT_CHOICES = (
    ('General Physicians', 'General Physicians'),
    ('Pediatric', 'Pediatric'),
    ('Cardiology', 'Cardiologist'),
    ('Gynecology', 'Gynecology'),
    ('Ortho', 'Ortho'),
    ('ENT', 'ENT'),
    ('oncology', 'oncology'),
)


class DoctorRegister(forms.ModelForm):
    phone_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)

    class Meta:
        model = Doctor
        fields = ('name', 'phone_no', 'email', 'department')


class PatientRegister(forms.ModelForm):
    phone_no = forms.CharField(validators=[phone_number_validator])
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)

    class Meta:
        model = Patient
        fields = ('name', 'phone_no', 'address', 'age', 'gender', 'department')


class SpecialistRegister(forms.ModelForm):
    phone_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)

    class Meta:
        model = Specialist
        fields = ('name', 'phone_no', 'email', 'department')


class UploadReport(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('description',)
        widgets = {
            'report': forms.FileInput(attrs={'class': 'form-control'})
        }


class ReferForm(forms.ModelForm):
    class Meta:
        model = Refer
        fields = ('patient', 'referred_to')


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title', 'content',)


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('date','patient','Doctors_note','Medicine_name',)


class XrayForm(forms.ModelForm):
    class Meta:
        model = drsharereport
        fields =('__all__')


