# Generated by Django 4.0.6 on 2022-08-04 11:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import health_data_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_specialist', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=300)),
                ('phone_no', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=300)),
                ('phone_no', models.CharField(max_length=300)),
                ('address', models.TextField(max_length=300)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=300)),
                ('verified', models.BooleanField(default=False)),
                ('rshare1', models.FileField(null=True, upload_to=health_data_app.models.uploaded_location)),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=300)),
                ('phone_no', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='spsharedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField(null=True)),
                ('sp_shareimage', models.FileField(null=True, upload_to=health_data_app.models.uploaded_location)),
                ('sp_userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
                ('speciaisdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.specialist')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(null=True, upload_to=health_data_app.models.uploaded_location)),
                ('rshare1', models.FileField(null=True, upload_to=health_data_app.models.uploaded_location)),
                ('rshare2', models.FileField(null=True, upload_to=health_data_app.models.uploaded_location)),
                ('description', models.TextField()),
                ('doctor_request', models.IntegerField(default=0)),
                ('specialist_request', models.IntegerField(default=0)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='health_data_app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
                ('specialist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='health_data_app.specialist')),
            ],
        ),
        migrations.CreateModel(
            name='Refer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
                ('referred_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='refer', to='health_data_app.doctor')),
                ('referred_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='refered_dr', to='health_data_app.specialist')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Doctors_note', models.TextField()),
                ('Medicine_name', models.CharField(max_length=300)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='drsharereport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('report', models.IntegerField(null=True)),
                ('report_image', models.FileField(null=True, upload_to='doc/')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='drsharedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField(null=True)),
                ('dr_shareimage', models.FileField(null=True, upload_to=health_data_app.models.uploaded_location)),
                ('docterdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.doctor')),
                ('dr_userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('replay', models.CharField(blank=True, max_length=300, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_data_app.patient')),
            ],
        ),
    ]
