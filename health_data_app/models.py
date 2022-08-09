from django.contrib.auth.models import AbstractUser
from django.db import models
from random import randrange


def uploaded_location(instance, filename):
    irand = randrange(0, 10)
    filename = str(irand) + '.png'
    print('name', filename)
    return "%s/%s" % ('crypto', filename)


class Login(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_specialist = models.BooleanField(default=False)


class Doctor(models.Model):
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=300)
    phone_no = models.CharField(max_length=300)
    email = models.EmailField()
    department = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    # rshare2 = models.FileField(upload_to =uploaded_location,null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=300)
    phone_no = models.CharField(max_length=300)
    address = models.TextField(max_length=300)
    age = models.IntegerField()

    gender = models.CharField(max_length=200)
    department = models.CharField(max_length=300)
    verified = models.BooleanField(default=False)
    rshare1 = models.FileField(upload_to=uploaded_location, null=True)

    def __str__(self):
        return self.name


class Specialist(models.Model):
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=300)
    phone_no = models.CharField(max_length=300)
    email = models.EmailField()
    department = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    # rshare2 = models.FileField(upload_to =uploaded_location,null=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # report = models.ImageField(upload_to='report')
    report = models.FileField(upload_to=uploaded_location, null=True)
    rshare1 = models.FileField(upload_to=uploaded_location, null=True)
    rshare2 = models.FileField(upload_to=uploaded_location, null=True)
    description = models.TextField()
    doctor_request = models.IntegerField(default=0)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True, blank=True)
    specialist_request = models.IntegerField(default=0)
    specialist = models.ForeignKey(Specialist, on_delete=models.DO_NOTHING, null=True, blank=True)

    # def __str__(self):
    #     return self.patient


class Refer(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_by = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, related_name='refer')
    # referred_to = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, related_name='refered_dr')
    referred_to = models.ForeignKey(Specialist, on_delete=models.DO_NOTHING, related_name='refered_dr')


class drsharedata(models.Model):
    report_id = models.IntegerField(null=True)
    dr_userdata = models.ForeignKey(Patient, on_delete=models.CASCADE)
    docterdata = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dr_shareimage = models.FileField(upload_to=uploaded_location, null=True)


class spsharedata(models.Model):
    report_id = models.IntegerField(null=True)
    sp_userdata = models.ForeignKey(Patient, on_delete=models.CASCADE)
    speciaisdata = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    sp_shareimage = models.FileField(upload_to=uploaded_location, null=True)


class Complaint(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_by = models.ForeignKey(Patient, on_delete=models.CASCADE)
    replay = models.CharField(max_length=300, null=True, blank=True)


class Prescription(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctors_note = models.TextField()
    Medicine_name = models.CharField(max_length=300)


class drsharereport(models.Model):
    name= models.CharField(max_length=50)
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    report = models.IntegerField(null=True)
    report_image = models.FileField(upload_to='doc/', null=True)