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


class User(AbstractUser):
    ROLES = [
        ('Admin', 'Admin'),
        ('Regular User', 'Regular User'),
    ]

    role = models.CharField(max_length=50, choices=ROLES)

    class Meta:
        # Add related_name to the groups and user_permissions fields
        permissions = [
            ('can_manage_gadgets', 'Can manage gadgets'),
            # Add more custom permissions as needed
        ]


User._meta.get_field(
    'groups').remote_field.related_name = 'device_mgt_user_groups'
User._meta.get_field(
    'user_permissions').remote_field.related_name = 'device_mgt_user_user_permissions'


def __str__(self):
    return self.username
