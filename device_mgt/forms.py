from django import forms
from .models import Gadget, AccessControl, AccessLog, User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
class IssueGadgetForm(forms.Form):
    gadget_type = forms.ChoiceField(label='Gadget Type', choices=[])  # Choices will be populated dynamically
    serial_number = forms.CharField(label='Serial Number', max_length=100)

class ReturnGadgetForm(forms.Form):
    serial_number = forms.CharField(label='Serial Number', max_length=100)




class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        fields = '__all__'

class AccessControlForm(forms.ModelForm):
    class Meta:
        model = AccessControl
        fields = '__all__'

class AccessLogForm(forms.ModelForm):
    class Meta:
        model = AccessLog
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

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