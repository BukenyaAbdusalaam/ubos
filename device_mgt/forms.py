from django import forms
from .models import Gadget, AccessControl, AccessLog, User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# class IssueGadgetForm(forms.Form):
#     gadget_type = forms.ChoiceField(label='Gadget Type', choices=[])  # Choices will be populated dynamically
#     serial_number = forms.CharField(label='Serial Number', max_length=100)

class IssueGadgetForm(forms.ModelForm):
    gadget_type = forms.ChoiceField(choices=Gadget.GADGET_TYPES, required=True)
    serial_number = forms.CharField(label='Serial Number', max_length=100)

    class Meta:
        model = Gadget
        fields = ['gadget_type', 'serial_number']


class ReturnGadgetForm(forms.Form):
    serial_number = forms.CharField(label='Serial Number', max_length=100)




class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        fields = ['gadget_type','serial_number']

class AccessControlForm(forms.ModelForm):
    class Meta:
        model = AccessControl
        fields = '__all__'

class AccessLogForm(forms.ModelForm):
    class Meta:
        model = AccessLog
        fields = '__all__'

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=128,required=True)
    role = forms.ChoiceField(choices=[('regular_user', 'Regular User'), ('admin', 'Admin')], required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'role']



class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=True)

    # Override the __init__ method to customize form initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'role') 