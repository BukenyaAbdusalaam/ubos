from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission


class Gadget(models.Model):
    GADGET_TYPES = [
        ('Tablet', 'Tablet'),
        ('Laptop', 'Laptop'),
        # Add other gadget types as needed
    ]

    gadget_id = models.AutoField(primary_key=True)
    gadget_type = models.CharField(max_length=50, choices=GADGET_TYPES)
    serial_number = models.CharField(max_length=100, unique=True)
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE)
    issued_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.gadget_type} - {self.serial_number}"


class AccessControl(models.Model):
    ROLES = [
        ('Admin', 'Admin'),
        ('Regular User', 'Regular User'),
    ]

    role = models.CharField(max_length=50, choices=ROLES, unique=True)
    access_control_config = models.TextField()

    def __str__(self):
        return self.role


class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20,default='')
    password = models.CharField(max_length=128,default='')
    role = models.CharField(max_length=20, choices=[('regular_user', 'Regular User'), ('admin', 'Admin')], default='regular_user')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
