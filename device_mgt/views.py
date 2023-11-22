from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import IssueGadgetForm, ReturnGadgetForm
from .models import Gadget, AccessControl, AccessLog, User
from django.utils import timezone
from .forms import GadgetForm, AccessControlForm, AccessLogForm, UserForm,CustomAuthenticationForm,CustomUserCreationForm
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
def manage_gadgets(request):
    gadgets = Gadget.objects.all()

    gadget_type_choices = Gadget.GADGET_TYPES

    issue_form = IssueGadgetForm(initial={'gadget_type': gadget_type_choices[0][0]})
    issue_form.fields['gadget_type'].choices = gadget_type_choices

    return_form = ReturnGadgetForm()

    return render(request, 'manage_gadgets.html', {'gadgets': gadgets, 'issue_form': issue_form, 'return_form': return_form})

    return render(request, 'manage_gadgets.html', {'gadget_types': gadget_types, 'gadgets': gadgets, 'issue_form': issue_form, 'return_form': return_form})


@user_passes_test(is_admin, login_url='/login/')
@login_required
def issue_gadget(request):
    gadget_types = [choice[0] for choice in Gadget.GADGET_TYPES]
    if request.method == 'POST':
        form = IssueGadgetForm(request.POST, choices={'gadget_type': gadget_types})

        if form.is_valid():
            gadget_type = form.cleaned_data['gadget_type']
            serial_number = form.cleaned_data['serial_number']

            # Check if the gadget with the given serial number exists
            gadget = Gadget.objects.filter(serial_number=serial_number).first()

            if gadget and gadget.issued_to is None:  # Check if the gadget exists and is not already issued
                gadget.issued_to = request.user
                gadget.issued_date = timezone.now()
                gadget.save()
                return redirect('manage_gadgets')  # Redirect to the gadget management page after successful issuance
    else:
        form = IssueGadgetForm(choices={'gadget_type': gadget_types})

    return render(request, 'manage_gadgets.html', {'issue_form': form, 'return_form': ReturnGadgetForm()})

@login_required
def return_gadget(request):
    if request.method == 'POST':
        form = ReturnGadgetForm(request.POST)

        if form.is_valid():
            serial_number = form.cleaned_data['serial_number']

            # Check if the gadget with the given serial number exists and is issued to the current user
            gadget = Gadget.objects.filter(serial_number=serial_number, issued_to=request.user).first()

            if gadget:  # Check if the gadget exists and is issued to the current user
                gadget.return_date = timezone.now()
                gadget.save()
                return redirect('manage_gadgets')  # Redirect to the gadget management page after successful return
    else:
        form = ReturnGadgetForm()

    return render(request, 'manage_gadgets.html', {'issue_form': IssueGadgetForm(), 'return_form': form})


from django.shortcuts import render, redirect

#@user_passes_test(is_admin, login_url='/')

def gadget_form(request):
    if request.method == 'POST':
        form = GadgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gadget_form')
    else:
        form = GadgetForm()

    return render(request, 'gadget_form.html', {'form': form})

@user_passes_test(is_admin, login_url='/login/')
def access_control_form(request):
    if request.method == 'POST':
        form = AccessControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access_control_form')
    else:
        form = AccessControlForm()

    return render(request, 'access_control_form.html', {'form': form})


@user_passes_test(is_admin, login_url='/login/')
def access_log_form(request):
    if request.method == 'POST':
        form = AccessLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access_log_form')
    else:
        form = AccessLogForm()

    return render(request, 'access_log_form.html', {'form': form})

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
             if User.objects.filter(email=email).exists():
                raise ValueError("Email address already exists.")
        form.save()

        return redirect('user_form')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})

@user_passes_test(is_admin, login_url='/login/')
def list_gadgets(request):
    gadgets = Gadget.objects.all()
    return render(request, 'list_gadgets.html', {'gadgets': gadgets})

@user_passes_test(is_admin, login_url='/login/')
def update_gadget(request, gadget_id):
    gadget = get_object_or_404(Gadget, pk=gadget_id)
    if request.method == 'POST':
        form = GadgetForm(request.POST, instance=gadget)
        if form.is_valid():
            form.save()
            return redirect('list_gadgets')
    else:
        form = GadgetForm(instance=gadget)

    return render(request, 'update_gadget.html', {'form': form, 'gadget': gadget})

@user_passes_test(is_admin, login_url='/login/')
def delete_gadget(request, gadget_id):
    gadget = get_object_or_404(Gadget, pk=gadget_id)
    if request.method == 'POST':
        gadget.delete()
        return redirect('list_gadgets')

    return render(request, 'delete_gadget.html', {'gadget': gadget})

def admin_dashboard(request):
    # Add logic or data retrieval as needed
    return render(request, 'admin_dashboard.html')

# class CustomLoginView(LoginView):
#     form_class = CustomAuthenticationForm
#     template_name = 'login.html'

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        this_user = authenticate(username=username, password=password)

        if this_user is not None:
            login(request, this_user)
            messages.success(request, 'Logged In')
            if this_user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('home')


        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return '/'

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email_address']
        password = request.POST['password']

        myUser = User.objects.create_user(
            username, email, password)

        myUser.is_active = True

        myUser.save()

        messages.success(request, "Personal account created Successfully...!")

        return redirect("login")

    context = {
        messages: 'messages'
    }
    return render(request, 'register_user.html')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    success_url = 'password_reset_done'
    email_template_name = 'password_reset_email.html'
    form_class = CustomAuthenticationForm

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = 'password_reset_complete'
    form_class = CustomAuthenticationForm
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

@login_required(login_url='login')
def signout(request):
    logout(request)
    messages.info(request, 'Logged Out..!')
    return redirect('login')

@login_required
def user_dashboard(request):
    # Fetch information related to the user, such as issued gadgets
    user_gadgets = Gadget.objects.filter(issued_to=request.user)

    return render(request, 'user_dashboard.html', {'user_gadgets': user_gadgets})